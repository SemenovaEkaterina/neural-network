import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


test_images, test_labels = mnist.train.next_batch(10000)


for i in range(0, len(test_images)):
    test_images[i] = np.array(test_images[i]) / 255


w = (2 * np.random.rand(10, 784) - 1) / 10
b = (2 * np.random.rand(10) - 1) / 10


for i in range(10):
    w[i] = np.loadtxt('train/{}'.format(i))

b = np.loadtxt('train/b')


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
    print("accuracy {} = {}".format(i, valid[i] / (total[i] + 0.000001)))
    print("total {} = {}".format(i, total[i]))


