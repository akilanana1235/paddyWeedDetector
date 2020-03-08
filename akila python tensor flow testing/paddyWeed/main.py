import tensorflow as tf
from tensorflow import keras

import numpy as np

fashion_mist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, trst_labels) = fashion_mist.load_data()

train_images.shape 
