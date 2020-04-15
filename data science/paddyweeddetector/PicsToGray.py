import numpy 
import os
import cv2
import random
import pickle

file_list = []
class_list = []

DATADIR = "D:\iit\year 2\SDGP\weed detector\paddyWeedDetector\Data_set\datatrain"
CATEGORIES = ["weed", "paddy"]
IMG_SIZE = 50

for category in CATEGORIES : #each in CATERGORIES
	path = os.path.join(DATADIR, category)
	for img in os.listdir(path):
		img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE) #reading the image and converting the image into gray scale
training_data = []


def create_training_data():
	for category in CATEGORIES :
		path = os.path.join(DATADIR, category)
		class_num = CATEGORIES.index(category)
		for img in os.listdir(path):
			try :
				img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
				new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
				training_data.append([new_array, class_num]) #add to the array
			except Exception as e:
				pass

create_training_data()

random.shuffle(training_data) #shuffling to reduce the time taken to process

X = [] #features
y = [] #labels

for features, label in training_data:
	X.append(features)
	y.append(label)

#resize the image for easy access

# X = numpy.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

X = numpy.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y = numpy.array(y)

# Creating the files containing all the information about the model
#open pickle file only for write
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

#open pickle file only to read
pickle_in = open("X.pickle", "rb")

#load it to the variable
X = pickle.load(pickle_in)