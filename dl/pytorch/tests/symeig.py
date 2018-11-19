import torch as th
from torch.autograd import Variable
import torch.nn as nn
from torch.autograd.function import Function
import torch.nn.functional as F

tensor = torch.randn(3, 3).cuda()
tensor = torch.mm(tensor, tensor.t())
eigval, eigvec = torch.symeig(tensor, eigenvectors=True)
