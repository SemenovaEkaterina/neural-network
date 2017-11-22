import os
import sys
import numpy as np
import matplotlib.pyplot as plt


import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

tr_images, tr_labels = mnist.train.next_batch(60000)

TRAIN_SIZE = 50000
SHOW_PROGRESS = False
NUMBER = 0

if len(sys.argv) > 1:
    if sys.argv[1] == 'progress':
        SHOW_PROGRESS = True

fig0 = plt.figure()

im0 = plt.imshow(np.asmatrix(tr_images[0].reshape(28, 28)), 'pink', animated=True)
# plt.ion()


for i in range(0, len(tr_images)):
    tr_images[i] = np.array(tr_images[i]) / 255

img_shape = (28, 28)


def relu(x):
    return np.maximum(x, 0)


w = (2 * np.random.rand(10, 784) - 1) / 10
b = (2 * np.random.rand(10) - 1) / 10

for n in range(len(tr_images)):
    print('Training: {}'.format(n)) if n % 10000 == 0 else None

    img = tr_images[n]
    cls = tr_labels[n]

    # forward propagation
    resp = np.zeros(10, dtype=np.float32)
    for i in range(0, 10):
        r = w[i] * img
        r = relu(np.sum(r) + b[i])
        resp[i] = r

    resp_cls = np.argmax(resp)
    resp = np.zeros(10, dtype=np.float32)
    resp[resp_cls] = 1.0

    # back propagation

    if isinstance(cls, int):
        true_resp = np.zeros(10)
        true_resp[cls] = 1
    else:
        true_resp = cls

    error = resp - true_resp

    delta = error * ((resp >= 0) * np.ones(10))
    for i in range(0, 10):
        w[i] -= np.dot(img, delta[i])
        b[i] -= delta[i]

    if SHOW_PROGRESS:
        im0.set_array(np.asmatrix(w[0].reshape(28, 28)))
        plt.pause(0.000001)


for i in range(10):
    filename = 'train/{}'.format(i)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    np.savetxt(filename, w[i])
    im0.set_array(np.asmatrix(w[i].reshape(28, 28)))
    filename = 'report/imgs/{}.png'.format(i)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    plt.savefig(filename)


filename = 'train/b'
np.savetxt(filename, b)