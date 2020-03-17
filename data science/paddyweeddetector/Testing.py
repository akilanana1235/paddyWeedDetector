import cv2
import tensorflow as tf

CATEGORIES = ["weed", "paddy"]


def prepare(filepath):
    IMG_SIZE = 70  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("CNN.model")

prediction = model.predict([prepare('D:\\paddyWeedDetector\\Data_set\\validation\\http___hasbrouck.asu.edu_imglib_seinet_DES_DES00071_DES00071576_lg.jpg')])
print(prediction)  # will be a list in a list.
print(CATEGORIES[int(prediction[0][0])])

# D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\Data_set\validation