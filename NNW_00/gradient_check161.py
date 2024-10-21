import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from TwoLayerNet158 import TwoLayerNet
from keras.dataset import mnist

#from tensorflow.keras.datasets import mnist

#(x_train, t_train), (x_test, t_test) = mnist.load_data()


(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

grand_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)

for key in grand_numerical.keys():
    diff = np.average( np.abs(grad_backprop[key] - grand_numerical[key]) )
    print(key + ":" + str(diff))

