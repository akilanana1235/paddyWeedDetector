import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

DATADIR = "D:\iit\year-2\SDGP\weed-detector\paddyWeedDetector\Data_set\datatrain" #path to the data set.
CATEGORIES = ["paddy", "weed"]

for category in CATEGORIES:
    path = os.path.join(DATADIR,category)  # create path to paddy and weed
    for img in os.listdir(path):  # iterate over each image per paddy and weed
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array and gray scaling
        plt.imshow(img_array, cmap='gray')  # graph it
        plt.show()  # display
        break  # to display one picture in gray scale
    break

print(img_array)

print(img_array.shape)

IMG_SIZE = 50 #resizing images to 50 by 50

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')
plt.show()

training_data = []

def create_training_data():
    for category in CATEGORIES:

        path = os.path.join(DATADIR,category)  # create path to paddy and weed
        class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=paddy 1=weed

        for img in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
                training_data.append([new_array, class_num])  # add this to training_data
            except Exception as e:  # in the interest in keeping the output clean...
                pass
            #except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            #except Exception as e:
            #    print("general exception", e, os.path.join(path,img))

create_training_data()

print(len(training_data))

import random

random.shuffle(training_data) #this will suffle the data and input to the modle.

for sample in training_data[:10]: #checking if the shuffling is working
    print(sample[1])

#making the modle
X = []
y = []

for features,label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

y = np.array(y)

import pickle #saving the processed data inside a picle

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

