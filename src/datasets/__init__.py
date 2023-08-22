from .mnist import MNIST, FashionMNIST
from .svhn import SVHN
from .cifar import CIFAR10, CIFAR100
from .utils import *

__all__ = ('MNIST', 'FashionMNIST',
           'SVHN',
           'CIFAR10', 'CIFAR100')