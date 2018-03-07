
import os
import argparse
import subprocess

# Example usage:
# python3 imageReciever.py 
# --image_file=/Users/alexanderdubilet/Pictures/dog.jpg \
# --model_dir=/Users/alexanderdubilet/Documents/oxd553/imagenet_model

def main (image_file, model_dir):
	request = "python3 " +"native_TF_scripts/classify_image.py "+ image_file +" "+ model_dir
	results  = os.popen(request).readlines()
	return (results)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument(
		'--image_file',
		required=True,
		type=str,
		help='Absolute path to image file.')

	parser.add_argument(
		'--model_dir',
		required=True,
		type=str,
		help="""\Path to the folder that contains: classify_image_graph_def.pb,imagenet_synset_to_human_label_map.txt, and imagenet_2012_challenge_label_map_proto.pbtxt.""")
	


	arguments = parser.parse_args()
	imageFileRequest = "--image_file="+arguments.image_file
	modelFileRequest = "--model_dir="+arguments.model_dir	
	print (imageFileRequest)
	print (modelFileRequest)
	output = main(imageFileRequest, modelFileRequest)
	print ()
	print ("These are our best guesses: ")
	print ()
	for guess in output:
		print (guess)