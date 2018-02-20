import os
import argparse
import subprocess

# Example usage: 
# python3 neuralNetworkTrainer.py \
# --image_dir=/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/animal_model/labeled_training_images \
# --output_graph=/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/animal_model/output_graph.pb \
# --output_labels=/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/animal_model/output_labels.txt \
# --bottleneck_dir=/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/animal_model/bottleneck_animals \
# --model_dir=/Users/alexanderdubilet/Documents/oxd553/imagenet_model
# --how_many_training_steps=10 --------[optional]-------

def main (
	image_dir, 
	output_graph, 
	output_labels, 
	bottleneck_dir,
	how_many_training_steps,
	model_dir
	):
	request = ("python3 " 
						+
						"native_TF_scripts/retrain.py "
						+ 
						image_dir,
						output_graph,
						output_labels,
						bottleneck_dir,
						how_many_training_steps,
						model_dir)
	request = ' '.join(request)   
	results = subprocess.call(request, shell=True)
	if results==0:
		return True
	else:
		return False
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument(
		'--image_dir',
		required=True,
		type=str,
		help='Absolute path to labeled training images.')

	parser.add_argument(
		'--output_graph',
		required=True,
		type=str,
		help='Save output graph to ... ')

	parser.add_argument(
		'--output_labels',
		required=True,
		type=str,
		help='Save output labels to ... ')

	# parser.add_argument(
	# 	'print_misclassified_files',
	# 	defualt=""
	# 	help='Do we print images we are unsure about? ')

	parser.add_argument(
		'--bottleneck_dir',
		required=True,
		type=str,
		help='Save bottleneck to ... ')
	parser.add_argument(
		'--how_many_training_steps',
		required=False,
		type=int,
		default=4000,
		help='How many training steps we want to make. Default is 4000 ')
	parser.add_argument(
		'--model_dir',
		required=True,
		type=str,
		help="Path to imagenet folder")

	arguments = parser.parse_args()
	
	imageDirRequest = "--image_dir="+arguments.image_dir
	outputGraphRequest = "--output_graph="+arguments.output_graph
	outputLabelsRequest = "--output_labels="+arguments.output_labels
	bottleneckRequest = "--bottleneck_dir="+arguments.bottleneck_dir
	if arguments.how_many_training_steps is not None: 
		trainingStepsRequest = "--how_many_training_steps="+str(arguments.how_many_training_steps)
	else: 
		trainingStepsRequest = 4000
	
	modelFileRequest = "--model_dir="+arguments.model_dir	
	
	
	print ("")
	output = main(imageDirRequest, outputGraphRequest, outputLabelsRequest, bottleneckRequest, trainingStepsRequest, modelFileRequest)
	print ("Operations successful: ", output)