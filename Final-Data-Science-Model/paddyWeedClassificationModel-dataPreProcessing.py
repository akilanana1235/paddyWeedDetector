import numpy as np
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

DATA_DIRECTORY = "D:\iit\year-2\SDGP\weed-detector\paddyWeedDetector\Data_set\datatrain" #path where the data set is located
CATEGORIES = ["paddy", "weed"]

for category in CATEGORIES:
    path = os.path.join(DATA_DIRECTORY, category)  # create path to paddy and weed
    for img in os.listdir(path):  # iterate over each image per paddy and weed
        gray_img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)  # convert to array and gray scaling
        plt.imshow(gray_img_array, cmap='gray')  # graph it
        plt.show()  # display
        break  # to display one picture in gray scale
    break

print(gray_img_array)

print(gray_img_array.shape)

IMAGE_SIZE = 50 #resizing images to 50 by 50

resize_img_array = cv2.resize(gray_img_array, (IMAGE_SIZE, IMAGE_SIZE)) #adding the resized images to an array
plt.imshow(resize_img_array, cmap='gray')
plt.show()

training_data_array = [] #training data array

def create_training_data():
    for category in CATEGORIES:

        path = os.path.join(DATA_DIRECTORY, category)  # create path to paddy and weed
        class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=paddy 1=weed

        for image in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
            try:
                image_array = cv2.imread(os.path.join(path, image), cv2.IMREAD_GRAYSCALE)  # convert to array
                image_array_2 = cv2.resize(image_array, (IMAGE_SIZE, IMAGE_SIZE))  # resize to normalize data size
                training_data_array.append([image_array_2, class_num])  # add this to training_data
            except Exception as e:  #to keep the output clean...
                pass

create_training_data()

print(len(training_data_array))

import random

#to balance the training data input to the model
random.shuffle(training_data_array) #this will suffle the data and input to the modle.

for sample in training_data_array[:10]: #checking if the shuffling is working
    print(sample[1])

#making the modle (pickles)
X = []
y = []

for features, label in training_data_array: #packeting the shuffled data to arrays
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1))

X = np.array(X).reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1)

y = np.array(y)

import pickle #saving the processed data inside a picle

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

#remember to remove

# pickle_in = open("X.pickle","rb")
# X = pickle.load(pickle_in)
#
# pickle_in = open("y.pickle","rb")
# y = pickle.load(pickle_in)