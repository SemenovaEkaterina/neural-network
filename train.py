import os
import numpy as np
import matplotlib.pyplot as plt


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


tr_images, tr_labels = mnist.train.next_batch(60000)


for i in range(0, len(tr_images)):
    tr_images[i] = np.array(tr_images[i]) / 255

img_shape = (28, 28)


def relu(x):
    return np.maximum(x, 0)


w = (2 * np.random.rand(10, 784) - 1) / 10
b = (2 * np.random.rand(10) - 1) / 10

number = 2

fig0 = plt.figure()

im0 = plt.imshow(np.asmatrix(w[number].reshape(28, 28)), 'pink', animated=True)
# plt.ion()

for n in range(len(tr_images)):
    print(n) if n % 40000 == 0 else None

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
    true_resp = cls

    error = resp - true_resp

    delta = error * ((resp >= 0) * np.ones(10))
    for i in range(0, 10):

        w[i] -= np.dot(img, delta[i])
        b[i] -= delta[i]

    # im0.set_array(np.asmatrix(w[number].reshape(28, 28)))
    # plt.pause(0.0000001)


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