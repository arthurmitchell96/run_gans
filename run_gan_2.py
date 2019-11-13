#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:50:01 2019

@author: socs-dual-boot
"""
import numpy
from keras.models import load_model
import os
from keras import backend as K
from keras.preprocessing.image import image 
#from PIL import Image
K.tensorflow_backend._get_available_gpus()
base_load_dir = (insert_here)#),'../sorted_and_cropped/instar4/','../sorted_and_cropped/instar5/','../sorted_and_cropped/instar6/')
folders_in_dir = (insert, here)
a = load_model(model name here, compile=False)
b = load_model(optional other model here, compile=False)

train = (optional if you have train and test dirs)
write_base_dir = save dectory here

#for normalising and denormalising inputs which is reqired for my generative networks
def normalize(input_data):

    return (input_data.astype(numpy.float32) - 127.5)/127.5 
def denormalize(input_data):
    input_data = (input_data + 1) * 127.5
    return input_data.astype(numpy.uint8)
#foes through each given file and runs every image through a generator
def create_imgs(direc, tot):
    p = os.listdir(base_load_dir+direc)
    
    for i in p:
        inp = image.load_img((base_load_dir+direc+i))
        #in this cvase i was running different sized images though different generators hence these if statements
        if ((inp.size[0]+inp.size[1])/2 < 100):
            inp = image.load_img((base_load_dir+direc+i), target_size=(60,60))
            inp = numpy.asarray(inp)
            inp = numpy.expand_dims(inp,axis=0)
            inp = normalize(inp)
            out = b.predict(inp)
            out = a.predict(out)
            output= out.reshape(240,240,3)
            output = denormalize(output)
            save = image.array_to_img(output)
            image.save_img((write_base_dir+tot+direc+i), save)
        elif ((inp.size[0]+inp.size[1])/2 < 250):
            inp = image.load_img((base_load_dir+direc+i), target_size=(120,120))
            inp = numpy.asarray(inp)
            inp = numpy.expand_dims(inp,axis=0)
            inp = normalize(inp)
            out = a.predict(inp)
            output= out.reshape(240,240,3)
            #output = out[0,:,:,:]
            output = denormalize(output)
            save = image.array_to_img(output)
            image.save_img((write_base_dir+tot+direc+i), save)
        else:
            inp2 = image.load_img((base_load_dir+direc+i),target_size=(240,240))
            #save = inp2.reszie((240,240))
            inp2.save((write_base_dir+tot+direc+i))
        
 #cycles through the directories        
for t in train:        
    for i in instars:
        create_imgs(i,t)