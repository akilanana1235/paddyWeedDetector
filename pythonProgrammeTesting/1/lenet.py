from tensorflow import keras
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

mypath = 'D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\pythonProgrammeTesting'

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=40,
    width_shift_range=0.15,
    height_shift_range=0.15,
    shear_range=0.15,
    zoom_range=0.15,
    horizontal_flip=True,
    fill_mode='nearest')

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    "D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\Data_set\datatrain", target_size=(150, 150), batch_size=20, class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    "D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\Data_set\lidating", target_size=(150, 150), batch_size=20, class_mode='binary')

model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    keras.layers.MaxPool2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(2, 2),
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(2, 2),
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(2, 2),
    keras.layers.Flatten(),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')])

model.summary()

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['acc'])

history = model.fit_generator(train_generator, steps_per_epoch=100, epochs=80, validation_data=validation_generator,
                              validation_steps=50)

model.save('cats_and_dogs_small_1.h5')
acc_train = history.history['acc']
acc_val = history.history['val_acc']
epochs = range(1, 81)
plt.plot(epochs, acc_train, 'g', label='training accuracy')
plt.plot(epochs, acc_val, 'b', label='validation accuracy')
plt.title('Training and Validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()