import os
import argparse
import subprocess

# python3 customModelClassifier.py \
# --image=/Users/alexanderdubilet/Pictures/dog.jpg \
# --graph=/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/animal_model/output_graph.pb \
# --labels=/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/animal_model/output_labels.txt

def main (image, graph, labels):
	request = "python3 " +"native_TF_scripts/label_image.py", image, graph, labels
	
	request = ' '.join(request)
	results  = os.popen(request).readlines()
	return (results)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument(
		'--image',
		required=True,
		type=str,
		help='Absolute path to image file.')

	parser.add_argument(
		'--graph',
		required=True,
		type=str,
		help='Absolute path to graph.pb file.')

	parser.add_argument(
		'--labels',
		required=True,
		type=str,
		help="Absolute path to labels.txt file")
	


	arguments = parser.parse_args()
	imageFileRequest = "--image="+arguments.image
	graphRequest = "--graph="+arguments.graph
	labelsRequest = "--labels="+arguments.labels

	output = main(imageFileRequest, graphRequest, labelsRequest)
	
	# print (output)
	print ("These are our best guesses: ")
	print ()
	for guess in output:
		print (guess)