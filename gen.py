# -*- coding: UTF-8 -*-
import pygame
from PIL import Image
from io import StringIO
import io
import os, sys
import random

pygame.init()

f = open('word.txt', 'r', encoding="utf-8")
words = f.readline().strip()
f.close

def numRandom():
    return random.randint(0, 999999999999)

def saveImg(text, font, imgName, area = (5,3)):
    im = Image.new('RGB', (28,28), (255,255,255))
    rtext = font.render(text, True, (0,0,0), (255,255,255))
    sio = io.StringIO()
    pygame.image.save(rtext, imgName)
    line = Image.open(imgName)
    im.paste(line, area)
    im.save(imgName)

ttf = os.listdir('./ttf')
for n in range(len(ttf)):
    ttf[n] = './ttf/' + ttf[n]

for m in range(len(ttf)):
    font_path = ttf[m]
    font = pygame.font.Font(font_path, 25)
    os.chdir('./words')
    text_list = words.split(' ')
    length = len(text_list)
    
    for i in range(length):
        text = text_list[i].encode('utf-8').decode('utf-8')
        imgName = str(numRandom()) + '_' + text_list[i] + '_sample.png'
        if os.path.isfile(imgName):
            imgName = str(numRandom()) + str(numRandom()) + '_' + text_list[i] + '_sample.png'
            saveImg(text, font, imgName)
            continue
        else:
            try:
                saveImg(text, font, imgName)
            except:
                pass
    os.chdir('..')