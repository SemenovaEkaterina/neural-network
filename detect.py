import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


w = (2 * np.random.rand(10, 784) - 1) / 10
b = (2 * np.random.rand(10) - 1) / 10


for i in range(10):
    w[i] = np.loadtxt('train/{}'.format(i))

b = np.loadtxt('train/b')


def nn_calculate(img):
    resp = list(range(0, 10))
    for i in range(0, 10):
        # print(img)
        r = w[i] * img
        r = np.maximum(np.sum(r) + b[i], 0)  # relu
        resp[i] = r

    return np.argmax(resp)


def detect(img):
    predicted = nn_calculate(img)

    return predicted


