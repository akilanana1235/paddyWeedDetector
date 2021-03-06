import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

#importing the pickles we create
pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in)

X = X/255.0 #normalizing the data by scailing, min is 0 and max is 255

dense_layers = [2]
layer_sizes = [64, 128]
conv_layers = [3]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = "paddyweedCNN-{}-conv-{}-nodes-{}-dense-{}".format(conv_layer, layer_size, dense_layer, int(time.time()))
            tensorboard = TensorBoard(log_dir='logs\ {}'.format(NAME))
            print(NAME)

            # training the model
            model = Sequential()

            model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))  # Convolutional layer
            model.add(Activation('relu'))  # activation layer
            model.add(MaxPooling2D(pool_size=(2, 2)))  # max pooling layer

            for l in range(conv_layer - 1):
                model.add(Conv2D(layer_size, (3, 3)))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

            for l in range(dense_layer):
                model.add(Dense(512))  # dense layer
                model.add(Activation('relu'))
                model.add(Dropout(0.2))

            model.add(Dense(1))
            model.add(Activation('sigmoid'))

            model.compile(loss='binary_crossentropy',
                          optimizer='adam',
                          metrics=['accuracy'])

#how many items per round
model.fit(X, y, batch_size=30, epochs=10, validation_split=0.3, callbacks=[tensorboard])

#model.save('paddyWeedDetectionModelCNN.model') #saving the model

model.save('paddyWeedDetectorModelWithArch.h5') #saving the model with architecture to be upload