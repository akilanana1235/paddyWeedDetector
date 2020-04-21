from keras.applications.vgg16 import VGG16
model = VGG16(include_top=True, weights='imagenet')
model.save("VGG16.h5")