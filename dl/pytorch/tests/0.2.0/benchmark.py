# Quick Stress Test

import time
import torch
import argparse
import torchvision
import numpy as np
from torch.autograd import Variable
import torchvision.models as models
import torch.backends.cudnn as cudnn
import psutil
cudnn.benchmark = True

# Training settings
parser = argparse.ArgumentParser(description='PyTorch Quick Stress Test')
parser.add_argument('--batch-size', type=int, default=100, metavar='N',
                    help='input batch size for training (default: 100)')
parser.add_argument('--iteration', type=int, default=100, metavar='N',
                    help='number of iteration to test (default: 100)')
parser.add_argument('--warm-up-steps', type=int, default=5, metavar='N',
                    help='number of steps to train (default: 5)')
parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate (default: 0.01)')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='disables CUDA training')
parser.add_argument('--fp16', action='store_true', default=False,
                    help='Enable FP16 (Mixed Precision Training)')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                    help='how many steps to wait before logging training status')


args = parser.parse_args()
args.cuda = not args.no_cuda and torch.cuda.is_available()

torch.manual_seed(args.seed)
if args.cuda:
    torch.cuda.manual_seed(args.seed)

# Model ResNet if GPU detected, otherwise AlexNet
if args.cuda:
    net = models.resnet50()
else:
    net = models.alexnet()

# Log Info
print("-" * 64)
print("TEST INFO - PYTORCH STRESS TEST")
print("-" * 64)
print("PyTorch version:\t {}".format(torch.__version__))
print("Dataset:\t ImageNet Synthetic")
print("Data Format:\t NCHW (Channel First)")
print("Batch Size:\t {}".format(args.batch_size))
print("CUDA support:\t {}".format(torch.cuda.is_available()))

if torch.cuda.is_available():
    print("Model: \t ResNet50")
    print("Number of GPUs:\t {}".format(torch.cuda.device_count()))
else:
    print("Model: \t AlexNet")
    print("CPU cores:\t {}".format(psutil.cpu_count()))
print("=" * 64)

# Synthetic ImageNet Input (Data Format: Channel First)
inp = torch.randn(args.batch_size, 3, 224, 224)

# CUDA?
if args.cuda:
    net.cuda()
    inp = inp.cuda()

# MXP? (require CUDA enabled)
if args.cuda and args.fp16:
    net.half()
    inp = inp.half()

print("Warm Up")
# Warm Up
for i in range(args.warm_up_steps):
    net.zero_grad()
    out = net.forward(Variable(inp, requires_grad=True))
    loss = out.sum()
    loss.backward()

# if multipgpus
#torch.cuda.synchronize()

rate_list_accumulator = 0

print("Iteration \t Rate (Iter/s) \t Loss")
start=time.time()
for i in range(args.iteration):
    batch_start=time.time()
    net.zero_grad()
    out = net.forward(Variable(inp, requires_grad=True))
    loss = out.sum()
    loss.backward()
    batch_end=time.time()

    rate_list_accumulator += batch_end-batch_start
    # Logging
    if i != 0 and i % args.log_interval == 0:
        rate = args.log_interval/rate_list_accumulator
        print("{} \t {:.3f} ({:.3f} Imgs/s) \t {:.3f}".format(i, rate, rate*args.batch_size, -np.asscalar(loss.type(torch.FloatTensor).data.cpu().numpy())))
        rate_list_accumulator = 0
end=time.time()

# if multipgpus
#torch.cuda.synchronize()

final_rate = args.iteration/(end-start)
print("[Result on {} steps] Iterations per second: {:.3f} ( {:.3f} Imgs/s)".format(args.iteration, final_rate, final_rate*args.batch_size))
