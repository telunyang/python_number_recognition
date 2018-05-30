from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
import os, sys
import matplotlib.pyplot as plt

from keras.models import model_from_json



img = os.listdir('./words')

def read_image(img_name):
    im = Image.open(img_name).convert('L')
    data = np.array(im)
    return data

def read_label(img_name):
    basename = os.path.basename(img_name)
    data = basename.split('_')[0]
    return data

def plot_images_labels_prediction(images, labels, prediction, idx, num = 10):
    fig = plt.gcf()
    fig.set_size_inches(12,14)
    if num > 100: num = 100
    for i in range(0, num):
        ax = plt.subplot(10,10,1+i)
        ax.imshow(images[idx], cmap='binary')
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ", predict=" + str(prediction[idx])
        ax.set_title(title, fontsize=10)
        ax.set_xticks([]);ax.set_yticks([])
        idx+=1
    plt.show() 

images = []
labels = []

for fn in os.listdir('./words'):
    if fn.endswith('.png'):
        fn = os.path.join('./words', fn)
        images.append(read_image(fn))
        labels.append(read_label(fn))

y = np.array(labels)
X = np.array(images)
X = X.reshape(len(X), 784)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

plot_images_labels_prediction(images, labels, [], 0, 100)

batch_size = 200
nb_epoch = 200

model = Sequential()
model.add(Dense(units=512, input_dim=784, kernel_initializer='normal'))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(units=512, input_dim=784, kernel_initializer='normal'))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(units=10, kernel_initializer='normal'))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer = 'Adam',
              metrics=['accuracy'])

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

history = model.fit(
    X_train, 
    y_train,
    batch_size=batch_size,
    nb_epoch=nb_epoch,
    verbose=1,
    validation_data=(X_test, y_test))

scores = model.evaluate(X_test, y_test, verbose=0)

print('accuracy: ', scores[1])




json_string = model.to_json()
with open("model.config", "w") as text_file:
    text_file.write(json_string)

model.save_weights("model.weight")