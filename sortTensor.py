#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys 
import codecs
import subprocess


address = '/Users/alexanderdubilet/Desktop/iphone/toSortTogether'


for files in os.walk(address):
	# print "starts to parse address - ", address
	allFiles = files[2]
	for file in allFiles:
		# print "Accessing file: ", file
		accessPicture = subprocess.Popen('cd /Users/alexanderdubilet/Desktop/iphone/toSortTogether && file '+file, shell=True, stdout=subprocess.PIPE)
		accessPicture.wait()
		# print "1: ", accessPicture.returncode
		for line in accessPicture.stdout:
			# print "line: ", address+'/'+line
			tensorCommand = 'python3 /Users/alexanderdubilet/Documents/tensorflow/tensorflow/examples/image_retraining/label_image.py --graph=/Users/alexanderdubilet/Documents/tensorflow/tensorflow/examples/image_retraining/secretModel/output_graph.pb --labels=/Users/alexanderdubilet/Documents/tensorflow/tensorflow/examples/image_retraining/secretModel/output_labels.txt --image='
			# test = tensorCommand+address+'/'+file
			# print test
			tensorImage = subprocess.Popen(tensorCommand+address+'/'+file, shell=True, stdout=subprocess.PIPE)
			tensorImage.wait()	
			# print "2: ", tensorImage.returncode	
			
		
			
# print 'tensorCommand: ', tensorCommand+address+'/'+file
