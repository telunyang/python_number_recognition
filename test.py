import numpy as np
from keras.models import Sequential
from keras.models import model_from_json
from PIL import Image
import sys
import os
import csv

with open("model.config", "r") as text_file:
    json_string = text_file.read()

model = Sequential()
model = model_from_json(json_string)
model.load_weights("model.weight", by_name=False)

def createFileList(myDir, format='.png'):
    fileList = []
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# load the original image
myFileList = createFileList('./test')
 
for file in myFileList:
    #print('id: ', file)
    img_file = Image.open(file)
    filename = file.replace("./test\\", "")
    filename = filename.replace(".png", "")
    #print(filename)
    
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    img_grey = img_file.convert('L')
 
    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    #print(value)
    with open("./test/" + filename + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(value)


for i in range(0, 10): 
    X2 = np.genfromtxt('./test/' + str(i) + '.csv', delimiter=',').astype('float32')
    X1 = X2.reshape(1,784) / 255 
    predictions = model.predict_classes(X1) # get prediction result 
    print(predictions)