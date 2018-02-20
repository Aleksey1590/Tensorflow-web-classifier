#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import posixpath
import urllib
import cgi
import shutil
import mimetypes
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import codecs
import subprocess
import http.server
import argparse
import urllib.request, urllib.parse, urllib.error
from io import BytesIO
import time;

try:
	from StringIO import StringIO
except ImportError:
	from io import StringIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def startPage(self, path):
		"""Helper to produce a directory listing (absent index.html).
		Return value is either a file object, or None (indicating an
		error).  In either case, the headers are sent, making the
		interface the same as for send_head().
		"""

		
		file = BytesIO()
		displaypath = cgi.escape(urllib.parse.unquote(self.path))
		
		file.write(("<body>\n<h2>Hello world </h2>\n").encode())
		file.write(("<body>\n<h2>Welcome to Start Page </h2>\n").encode())
		file.write(("<body>\n<h2>Please, upload 1 image and we will try to guess what's depicted on it </h2>\n").encode())

		file.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
		file.write(b"<hr>\n")
		file.write(b"<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
		file.write(b"<input name=\"imageToClassify\" type=\"file\" accept=\"image/x-png,image/gif,image/jpeg\" />")
		file.write(b"<input type=\"submit\" value=\"Classify this image\"/></form>\n")
		
		file.write(b"\n")
		
		file.write(b"<hr>\n<ul>\n")
		length = file.tell()
		file.seek(0)
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.send_header("Content-Length", str(length))
		self.end_headers()
		return file



	def handleImageClassification(self):
		print ("_____")
		content_type = self.headers['content-type']
		if not content_type:
			return (False, "Content-Type header doesn't contain boundary")
		boundary = content_type.split("=")[1].encode()
		remainbytes = int(self.headers['content-length'])
		line = self.rfile.readline()
		remainbytes -= len(line)
		
		if not boundary in line:
			return (False, "Content NOT begin with boundary")
		line = self.rfile.readline()
		
		lineList = line.decode()
		lineList = lineList.split(";")
		
		remainbytes -= len(line)
		
		fileType = lineList[1]
		start_pt = fileType.find("\"")
		end_pt = fileType.find("\"", start_pt + 1)  # add one to skip the opening "
		fileType = fileType[start_pt + 1: end_pt]  # add one to get the quote excluding the ""
		print ("fileType: ", fileType)
		if not fileType:
			return (False, "Can't find what function is required...")
		filename = lineList[2]
		start_pt = filename.find("\"")
		end_pt = filename.find("\"", start_pt + 1)  # add one to skip the opening "
		filename = filename[start_pt + 1: end_pt]  # add one to get the quote excluding the ""
		print ("filename: ", filename)
		if not filename:
			return (False, "Can't find out file name...")

		path = self.translate_path(self.path)
		
		if not os.path.exists(path+"/"+filename):
			print ("Tried accessing file at: ", time.time())
			print ("Path + filename: ", path+"/"+filename)
			print ("doesnt exist")
		else:
			pass
		pass

		if fileType=="imageToClassify":
			labelClass = self.classifyImage(str(path), filename, (tfPath.Full_Path))
		else:
			return (False, "Unexpected mistake when determining fileType.")

		# labelClass = self.classifyImage(str(path), filename, (tfPath.Full_Path))
		fileFullPath = os.path.join(path, filename)
		line = self.rfile.readline()
		remainbytes -= len(line)
		line = self.rfile.readline()
		remainbytes -= len(line)
		try:
			out = open(fileFullPath, "wb")
		except IOError:
			return (False, "Can't create file to write, do you have permission to write?")
				
		preline = self.rfile.readline()
		remainbytes -= len(preline)
		while remainbytes > 0:
			line = self.rfile.readline()
			remainbytes -= len(line)
			if boundary in line:
				preline = preline[0:-1]
				if preline.endswith(b'\r'):
					preline = preline[0:-1]
				out.write(preline)
				out.close()
				return (True, "File '%s' upload success!" % fileFullPath, labelClass)
			else:
				out.write(preline)
				preline = line

		print ("_____")
		return (False, "Unexpect Ends of data.")

	

   

	def do_GET(self):
		"""Serve a GET request."""
		file = self.send_head()
		if file:
			print ("saving file at do_GET: ", time.time())
			shutil.copyfileobj(file, self.wfile)
			file.close()



	def do_HEAD(self):
		"""Serve a HEAD request."""
		file = self.send_head()
		if file:
			print ("saving file at do_HEAD: ", time.time())
			file.close()

	

	def do_POST(self):
		"""Serve a POST request."""
		
		response, info, labelClass = self.handleImageClassification()

		file = BytesIO()

			
		file.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
		file.write(b"<html>\n<title>Results Page</title>\n")
		file.write(b"<body>\n<h1>Results</h1>\n")
		file.write(b"<hr>\n")
		if (response==True):
			file.write(b"<strong>Success: </strong>")
		else:
			file.write(b"<strong>Failed: </strong>")
		file.write(info.encode())
		file.write(b"<hr>\n")
		file.write(b"<body>\n<h3>Your file has been successfully uploaded</h3>\n")
		file.write(b"<hr>\n")
		
		file.write(b'Classes: ')
		file.write(b"<p>")
		
		for index,label in enumerate(labelClass, start=1): 
			file.write(b"Guess: ")
			encodeInt = str(index)
			file.write(bytes(encodeInt.encode()))
			
			file.write(b"<p>")	
			
			file.write(bytes(label.encode()))
			file.write(b"<p>")	
		
		length = file.tell()
		file.seek(0)
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.send_header("Content-Length", str(length))
		self.end_headers()
		if file:
			print ("saving file at do_POST: ", time.time())
			shutil.copyfileobj(file, self.wfile)
			file.close()

	
	

	def send_head(self):
		"""Common code for GET and HEAD commands.
		This sends the response code and MIME headers.
		Return value is either a file object (which has to be copied
		to the outputfile by the caller unless the command was HEAD,
		and must be closed by the caller under all circumstances), or
		None, in which case the caller has nothing further to do.
		"""

		path = self.translate_path(self.path) 
		print ("path: ", path)	   
		file = None
		if os.path.isdir(path):
			if not self.path.endswith('/'):
				# redirect browser - doing basically what apache does
				self.send_response(301)
				self.send_header("Location", self.path + "/")
				self.end_headers()
				return None
			for index in "index.html", "index.htm":
				index = os.path.join(path, index)
				if os.path.exists(index):
					path = index
					break
			else:
				return self.startPage(path)
		
		try:
			# Always read in binary mode. Opening files in text mode may cause
			# newline translations, making the actual size of the content
			# transmitted *less* than the content-length!
			file = codecs.open(path, "rb", "utf-8")
		except IOError:
			self.send_error(404, "File not found")
			return None
		self.send_response(200)
		fs = os.fstat(file.fileno())
		# print ("fs", fs)
		self.send_header("Content-Length", str(fs[6]))
		self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
		self.end_headers()
		return file

	

	

	def translate_path(self, path):
		"""Translate a /-separated PATH to the local filename syntax.
		Components that mean special things to the local file system
		(e.g. drive or directory names) are ignored.  (XXX They should
		probably be diagnosed.)
		"""
		# abandon query parameters
		path = path.split('?',1)[0]
		path = path.split('#',1)[0]
		path = posixpath.normpath(urllib.parse.unquote(path))
		words = path.split('/')
		words = [_f for _f in words if _f]
		path = os.getcwd()
		for word in words:
			drive, word = os.path.splitdrive(word)
			head, word = os.path.split(word)
			if word in (os.curdir, os.pardir): continue
			path = os.path.join(path, word)
		return path


	
	def classifyImage(self, imagePath, imageName, tensorflowClassifyPath):
		print ("classifyImage: ", imagePath, imageName, tensorflowClassifyPath)
		tensorflow_classify_image = "python3 " + tensorflowClassifyPath[0]
		image_file = " --image_file="+imagePath+"/"+imageName
		request = tensorflow_classify_image + image_file
		print ("trying request: ", request)
		
		# Returns a list of arguments Tensorflow has provided us with
		pipe  = os.popen(request).readlines()
		return pipe


	

def test(tensorflow_classify_image,
		HandlerClass = SimpleHTTPRequestHandler,
		 ServerClass = HTTPServer):
	server_address = ('', 8000)	
	httpd = ServerClass(server_address, HandlerClass)
	httpd.serve_forever()
		

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Please, insert a full path to your Tensorflow classify_image.py file. \n It should be something like that: tensorflow/models/tutorials/image/imagenet/classify_image.py')
	parser.add_argument('Full_Path', help="Insert full path address of classify_image.py" ,metavar='Path', type=str, nargs='+')	
	tfPath = parser.parse_args()

	test(tfPath)

