import numpy as np
import os
import matplotlib.pyplot as plt

# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


# test_images, test_labels = mnist.train.next_batch(10000)



from mnist.loader import MNIST

import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

test_images, test_labels = mnist.train.next_batch(10000)


for i in range(0, len(test_images)):
    test_images[i] = np.array(test_images[i]) / 255


w = (2 * np.random.rand(10, 784) - 1) / 10
b = (2 * np.random.rand(10) - 1) / 10


for i in range(10):
    w[i] = np.loadtxt('train/{}'.format(i))

b = np.loadtxt('train/b')

dif = 1


def nn_calculate(img, log=False):
    resp = list(range(0, 10))
    for i in range(0, 10):
        r = w[i] * img
        # if log:
            # print(i, r)
        r = np.maximum(np.sum(r) + b[i], 0)  # relu
        if log:
            print(i, r)
        resp[i] = r
        if log:
            print(i, resp[i])
    if log:
        np.argmax(resp)

    return np.argmax(resp)


total = [0 for i in range(10)]
total_all = len(test_images)
valid = [0 for i in range(10)]
valid_all = 0
invalid = []


def index_of_first(lst):
    for i,v in enumerate(lst):
        if v == 1:
            return i
    return None


for i in range(0, len(test_images)):
    img = test_images[i]
    predicted = nn_calculate(img)
    true = test_labels[i]

    predicted_array = np.zeros(10, dtype=np.float32)
    predicted_array[predicted] = 1.0

    if isinstance(true, int):
        index = true
    else:
        index = index_of_first(true)
    if (predicted_array == true).all():
        valid[index] = valid[index] + dif
        valid_all += dif
    else:
        # predicted = nn_calculate(img, True)
        # print(true)

        # fig0 = plt.figure()

        # im0 = plt.imshow(np.asmatrix(img.reshape(28, 28)), 'pink', animated=True)
        # plt.show()
        # sys.exit()
        invalid.append({"image": img, "predicted": predicted, "true": true})
    total[index] = total[index] + 1
    total_all += 1


for i in range(10):
    # print("accuracy {} = {}".format(i, valid[i] / (total[i] + 0.000001)))
    f = open('report/stat/{}'.format(i), 'w')
    f.write(str(valid[i]/total[i])+';'+str(valid[i]))
    f.close()
    #print("total {} = {}".format(i, total[i]))
