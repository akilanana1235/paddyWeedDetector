from django.shortcuts import render
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from django.core.files.storage import FileSystemStorage

from keras.models import load_model
import numpy as np

from keras.preprocessing import image
import tensorflow as tf
import cv2
import json
from tensorflow import Graph, Session

categories = ["paddy", "weed"]

model_graph = Graph()
with model_graph.as_default():
    tf_session = Session()
    with tf_session.as_default():
        model=tf.keras.models.load_model('./model/paddyWeedDetectorModelWithArch.h5')

IMG_SIZE = 50




# Create your views here.

def index(request):
    context = {'a': 1}
    return render(request, 'index.html', context)

def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj=request.FILES['filePath']
    print('filePath')
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name, fileObj)
    filePathName=fs.url(filePathName)
    testimage = '.' + filePathName

    img = image.load_img(testimage, target_size=(IMG_SIZE, IMG_SIZE))
    x = image.img_to_array(img)
    x = cv2.imread(testimage, cv2.IMREAD_GRAYSCALE)
    x = cv2.resize(x, (IMG_SIZE, IMG_SIZE))

    x = x.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    with model_graph.as_default():
        with tf_session.as_default():
            prediction1 = model.predict(x)


    predictedLabel = (categories[int(prediction1[0][0])])

    context = {'filePathName': filePathName, 'predictedLabel': predictedLabel}
    return render(request, 'index.html', context)




