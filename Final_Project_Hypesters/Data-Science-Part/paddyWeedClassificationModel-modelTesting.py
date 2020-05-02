import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import tensorflow as tf

CATEGORIES = ["paddy", "weed"]  # will use this to convert prediction num to string value

def prepare(filepath):
    IMAGE_SIZE = 50  # 50 in txt-based
    image_grayscale_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
    image_resize_array = cv2.resize(image_grayscale_array, (IMAGE_SIZE, IMAGE_SIZE))  # resize image to match model's expected sizing
    return image_resize_array.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1)  # return the image with shaping that TF wants.

model = tf.keras.models.load_model("paddyWeedDetectorModelWithArch.h5")

prediction = model.predict([prepare('African-Lovegrass-BuckleyEcologyLab.jpeg')])  # PASSING A LIST OF THINGS YOU WISH TO PREDICT
print(CATEGORIES[int(prediction[0][0])])






















