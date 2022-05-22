import torch
from torchtext.datasets import AG_NEWS
train_iter = iter(AG_NEWS(split='train'))
