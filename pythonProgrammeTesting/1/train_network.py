# set the matplotlib backend so figures can be saved in the background
import random

import cv2
import matplotlib
from imutils import paths
from keras_preprocessing.image import img_to_array

matplotlib.use("Agg")
# import the necessary packages
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
dataset == "D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\Data_set";
ap.add_argument("-d", "--dataset", required=True,
                help="D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\Data_set")
ap.add_argument("-m", "--model", required=True,
                help="D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\pythonProgrammeTesting")
ap.add_argument("-p", "--plot", type=str, default="plot.png",
                help="D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\pythonProgrammeTesting")
args = vars(ap.parse_args())

# initialize the number of epochs to train for, initial learning rate,
# and batch size
EPOCHS = 25
INIT_LR = 1e-3
BS = 32
# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []
# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

# loop over the input images
for imagePath in imagePaths:
    # load the image, pre-process it, and store it in the data list
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    data.append(image)
    # extract the class label from the image path and update the
    # labels list
    label = imagePath.split(cv2.os.path.sep)[-2]
    label = 1 if label == "santa" else 0
    labels.append(label)
