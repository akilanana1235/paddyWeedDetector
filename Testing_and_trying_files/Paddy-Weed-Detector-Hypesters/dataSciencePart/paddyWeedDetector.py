import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import tensorflow as tf

CATEGORIES = ["paddy", "weed"]  # will use this to convert prediction num to string value

def prepare(filepath):
    IMG_SIZE = 50  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)  # return the image with shaping that TF wants.

model = tf.keras.models.load_model("paddyWeedDetectorModelWithArch.h5")

prediction = model.predict([prepare('IMG-20200321-WA0005.jpg')])  # PASSING A LIST OF THINGS YOU WISH TO PREDICT
print(CATEGORIES[int(prediction[0][0])])