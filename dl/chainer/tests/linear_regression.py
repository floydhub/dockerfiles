#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
from chainer import Variable, optimizers
import chainer.functions as F
import chainer.links as L

# Create 2 chainer variables then sum their squares
# and assign it to a third variable.
a = Variable(np.array([3], dtype=np.float32))
b = Variable(np.array([4], dtype=np.float32))
c = a**2 + b**2

# Inspect the value of your variables.
print("a.data: {0}, b.data: {1}, c.data: {2}".format(a.data, b.data, c.data))

c.backward()

# And inspect the gradients.
print("dc/da = {0}, dc/db = {1}, dc/dc = {2}".format(a.grad, b.grad, c.grad))

# Generate linearly related datasets x and y.

x = 30*np.random.rand(1000).astype(np.float32)
y = 7*x+10
y += 10*np.random.randn(1000).astype(np.float32)

# Setup linear link from one variable to another.

linear_function = L.Linear(1, 1)

# Set x and y as chainer variables, make sure to reshape
# them to give one value at a time.
x_var = Variable(x.reshape(1000, -1))
y_var = Variable(y.reshape(1000, -1))

# Setup the optimizer.
optimizer = optimizers.MomentumSGD(lr=0.001)
optimizer.setup(linear_function)


# Define a forward pass function taking the data as input.
# and the linear function as output.
def linear_forward(data):
    return linear_function(data)


# Define a training function given the input data, target data,
# and number of epochs to train over.
def linear_train(train_data, train_target, n_epochs=200):
    for _ in range(n_epochs):
        # Get the result of the forward pass.
        output = linear_forward(train_data)

        # Calculate the loss between the training data and target data.
        loss = F.mean_squared_error(train_target, output)

        # Zero all gradients before updating them.
        linear_function.zerograds()

        # Calculate and update all gradients.
        loss.backward()

        # Use the optmizer to move all parameters of the network
        # to values which will reduce the loss.
        optimizer.update()

for i in range(150):
    linear_train(x_var, y_var, n_epochs=5)
    y_pred = linear_forward(x_var).data

print('Done.')
