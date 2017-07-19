-- LUA WARNINGS
-- Array starts from index 1
-- obj.func() is equivalent to obj:func()
-- Loop:
--    for start_, end_ do
--    end
-- Condition:
--    if <condition> then
--    end
-- Function:
--    func_name = function(arguments)
--    <do stuff>
--    end
-- require: load module
-- OOP: Object is metatable.
-- Table and Array use {} to create.
require 'nn';

-- Spequentail or Concat or Parallel
net = nn.Sequential()
-- Every neural network module in Torch has automatic differentiation.
-- It has a :forword(input) method that computes the output for a given input
-- Flowing the inpt through the net.
-- It also has :backward(input, gradient) method that differentiates each
-- neuron in the net.

-- Layers
-- Torch supports many layers for your net.
-- See more: https://github.com/torch/nn/blob/master/doc/convolution.md
-- It also updates many state-of-the-art architectures and different kind of layers.
-- 3 input image plane
-- 6 output planes
-- 5x5 filter
-- (dW, dH) step
-- (padW, padH) padding
net:add(nn.SpatialConvolution(3, 6, 5, 5)) -- add a new spatial convolution layer
                                -- to the net
net:add(nn.ReLU()) -- add ReLU layer

-- SpatialMaxPooling: apply 2D max-pooling operation
-- in kW-kH regions by step size dWxdH, padding padWxpadH
-- SpatialMaxPooling(kW, kH, [ dW, dH, padW, padH])
-- 2x2 regions, step 2x2
net:add(nn.SpatialMaxPooling(2, 2, 2, 2))

-- Convolution layer
-- Input layers: 6 planes
-- Output layers: 16 planes
-- Kernel size: 5x5
net:add(nn.SpatialConvolution(6, 16, 5, 5))
-- apply Relu
net:add(nn.ReLU())
net:add(nn.SpatialMaxPooling(2, 2, 2, 2))
-- reshape tensor with size 16*5*5 into 1D vector with length 16*5*5
net:add(nn.View(16*5*5))

-- Apply fully connected layer
net:add(nn.Linear(16*5*5, 120))

net:add(nn.ReLU())
net:add(nn.Linear(120, 84))
net:add(nn.ReLU())
net:add(nn.Linear(84, 10))
net:add(nn.LogSoftMax())

print ("Lenet5\n" .. net:__tostring());
-- Create input data
input = torch.rand(3, 32, 32)
-- Feed the input to the net
output = net:forward(input)
-- zero the internal gradients
net:zeroGradParameters()

-- Defining a loss function
-- Link: https://github.com/torch/nn/blob/master/doc/criterion.md
-- Many defined loss functions
criterion = nn.ClassNLLCriterion() -- a nagative log-likelihood criterion

-- criterion has 2 main methods:
--  (1) :forward(input, target): calculates loss value based input and target value
--  (2) :backward(input, target): calculates the gradient of the loss function
--            associated to the cirterion and return the result.


loss = criterion:forward(output, 3)
gradients = criterion:backward(output, 3)
gradInput = net:backward(input, gradients)

-- Learnable parameters
m = nn.SpatialConvolution(1, 3, 2, 2) -- 1 plane input, 3 2x2 Convolution filters
-- Every layer having learnable parameters has 2 properties:
-- (1) : m.weights
-- (2) : m.bias
--
-- Update rule: weight = weight + learningRate * gradWeights
-- TRAINING PHASE

-- Loading data
-- e.x: CIFAR 10
-- Uncomment to download CIFAR 10
os.execute("wget -c https://s3.amazonaws.com/torch7/data/cifar10torchsmall.zip")
os.execute("unzip cifar10torchsmall.zip")

train_set = torch.load("cifar10-train.t7")
test_set = torch.load("cifar10-test.t7")

classes = { "airplane", "automobile", "bird", "cat", "deer",
            "dog", "frog", "horse", "ship", "truck" }

-- Torch supports Stochastic Gradient
-- To use it, the training data must have :size() function and
-- index operator ([index])
-- add index operator to the training set
setmetatable(train_set,
{
  __index = function(t, i)
    return {t.data[i], t.label[i]}
  end
});

train_set.data = train_set.data:double() -- convert to double type

function train_set:size()
  return self.data:size(1)
end

-- Preprocess data
-- zero mean data
mean = {}
stdv = {}
for i=1, 3 do -- each channel in the image
  mean[i] = train_set.data[ {{}, {i}, {}, {}} ]:mean() -- mean estimation
  train_set.data[{{}, {i}, {}, {}}]:add(-mean[i]) -- mean subtraction

  stdv[i] = train_set.data[{{}, {i}, {}, {}}]:std() -- std estimation
  train_set.data[{ {}, {i}, {}, {} }]:div(stdv[i]) -- std scaling
end

-- train the data
trainer = nn.StochasticGradient(net, criterion)
trainer.learningRate = 0.001
trainer.maxIteration = 5

trainer:train(train_set)
-- test the net
test_set.data = test_set.data:double() -- convert from byte to double
-- preprocess data
for i=1, 3 do
  test_set.data[{{}, {i}, {}, {}}]:add(-mean[i])
  test_set.data[{{}, {i}, {}, {}}]:div(stdv[i])
end

predicted = net:forward(test_set.data[100])
predicted:exp()

for i=1,predicted:size(1) do
  print(classes[i], predicted[i])
end

-- measure the accuracy
class_perf = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
accuracy = 0

for i=1,10000 do
  local groundtruth = test_set.label[i]
  local prediction = net:forward(test_set.data[i])
  local conf, indexes = torch.sort(prediction, true)
  if (groundtruth == indexes[1]) then
    class_perf[groundtruth] = class_perf[groundtruth] + 1
    accuracy = accuracy + 1
  end
end

for i=1, #classes do
  print(classes[i], 100*class_perf[i]/1000 .. " %")
end

print("Accuracy: ", accuracy * 100 / 10000 .. " . %")
