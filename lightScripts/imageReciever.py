import os
import argparse
import subprocess


def main (imagePath, modelPath):
	request = "python3 " +"classify_image.py "+ imagePath +" "+ modelPath
	results  = os.popen(request).readlines()
	return (results)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument(
		'image_file',
		type=str,
		help='Absolute path to image file.')

	parser.add_argument(
		'model_dir',
		type=str,
		help="""\Path to the folder that contains: classify_image_graph_def.pb,imagenet_synset_to_human_label_map.txt, and imagenet_2012_challenge_label_map_proto.pbtxt.""")
	


	arguments = parser.parse_args()
	imageFileRequest = "--image_file="+arguments.image_file
	modelFileRequest = "--model_dir="+arguments.model_dir	
	output = main(imageFileRequest, modelFileRequest)
	print ()
	print ("These are our best guesses: ")
	print ()
	for guess in output:
		print (guess)