import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle

NAME = "Weeds-vs-Paddy-CNN"

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu')) #rectified linear unit
model.add(MaxPooling2D(pool_size=(2, 2))) # downsample

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())  # convert 3D feature maps to 1D feature vectors
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

#model.compile(loss='binary_crossentropy',
#              optimizer='adam',
#              metrics=['accuracy'],
#              )


#40 iterations
looped = model.fit(X, y, batch_size=32, epochs=40, validation_split=0.1)


model.fit(X, y,
          batch_size=32,
          epochs=40,
          validation_split=0.3,
          callbacks=[tensorboard]
          )

#Graph plotting

#print(looped.history.keys())
#plt.figure(1)
#plt.plot(looped.history['acc'])
#plt.plot(looped.history['val_acc'])
#plt.title('model accuracy')
#plt.ylabel('accuracy')
#plt.xlabel('epoch')
#plt.legend(['train', 'validation'], loc='upper left')