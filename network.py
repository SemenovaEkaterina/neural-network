import numpy as np
import matplotlib.pyplot as plt


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


tr_images, tr_labels = mnist.train.next_batch(50000)
test_images, test_labels = mnist.train.next_batch(10000)


for i in range(0, len(test_images)):
    test_images[i] = np.array(test_images[i]) / 255

for i in range(0, len(tr_images)):
    tr_images[i] = np.array(tr_images[i]) / 255

img_shape = (28, 28)


def relu(x):
    return np.maximum(x, 0)


w = (2 * np.random.rand(10, 784) - 1) / 10
b = (2 * np.random.rand(10) - 1) / 10

number = 0

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

        w[i] -= np.dot(img, delta[i])*2
        # if (np.dot(img, delta[i]) != 0).any():
        #   print(i)
        b[i] -= delta[i]

    # im0.set_array(np.asmatrix(w[number].reshape(28, 28)))
    # plt.pause(0.0000001)


def nn_calculate(img):
    resp = list(range(0, 10))
    for i in range(0, 10):
        r = w[i] * img
        r = np.maximum(np.sum(r) + b[i], 0)  # relu
        resp[i] = r

    return np.argmax(resp)


total = [0 for i in range(10)]
valid = [0 for i in range(10)]
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


    index = index_of_first(true)
    if (predicted_array == true).all():
        valid[index] = valid[index] + 1
    else:
        invalid.append({"image": img, "predicted": predicted, "true": true})
    total[index] = total[index] + 1


for i in range(10):
    im0.set_array(np.asmatrix(w[i].reshape(28, 28)))
    plt.savefig('{}.png'.format(i))
    print("accuracy {} = {}".format(i, valid[i] / total[i]))
    print("total {} = {}".format(i, total[i]))
