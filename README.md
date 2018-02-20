Program uses Python 3

Image Recognition

1. Download/Clone imagenet_model AND lightScripts [Ignore webInterface]
2. Launch imageReciever.py in terminal by entering `python3 imageReciever.py image_file=<imagePath> model_dir=<modelDir>` where `imagePath` is Absolute Path to the image we want to recognize and `modelDir` is Absolute Path to Model folder (see help usage for more info)  
Example: 
`python3 imageReciever.py \

--image_file=/Users/alexanderdubilet/Pictures/dog.jpg \  
--model_dir=/Users/alexanderdubilet/Documents/oxd553/imagenet_model`  

3. You will receive an output in the terminal of classifier's guesses

Training Neural Network:
1. Download/Clone imagenet_model AND lightScripts [Ignore webInterface]
2. Launch neuralNetworkTrainer.py in terminal by entering  
```python3 neuralNetworkTrainer.py \    
--image_dir=<image_dir> \  
--output_graph=<output_graph> \  
--output_labels=<output_labels> \  
--bottleneck_dir=<bottleneck_dir> \  
--model_dir=<model_dir> \  
--how_many_training_steps=3450```  

3. Run  ```python3 neuralNetworkTrainer.py -h``` for more information about the arguments and what they do
4. Script also takes an optional argument of how many training steps it needs to perform. Defualt is 4000 which will take approx 30 mins. For developemnt/testing, I suggest to turn it down to 10
Example:  
```python3 neuralNetworkTrainer.py \  
--image_dir=/oxd553/lightScripts/custom_models/animal_model/labeled_training_images \  
--output_graph=/oxd553/lightScripts/custom_models/animal_model/output_graph.pb \  
--output_labels=/oxd553/lightScripts/custom_models/animal_model/output_labels.txt \  
--bottleneck_dir=/oxd553/lightScripts/custom_models/animal_model/bottleneck_animals \  
--model_dir=/oxd553/imagenet_model  
--how_many_training_steps=10```  
5. After script has finished running - it should says so in the terminal
6. Now you can use your custom model! Recognize unlabeled images with retrained model like this: ```python3 label_image.py --graph=retrained_graph.pb --labels=retrained_labels.txt --image=flower_photos/daisy/54377391_15648e8d18.jpg```
 
Using retrained Neural Network (more info can be found here - https://www.tensorflow.org/tutorials/image_retraining)

1. Download/Clone imagenet_model AND lightScripts [Ignore webInterface]
2. Run label_image.py found in native_TF_scripts like this: ```python3 label_image.py --graph=<retrained_graph.pb> --labels=<retrained_labels.txt> --image=<new_image.jpg> ```  
Example:  
```python3 customModelClassifier.py \  
--image='<your_file_path>'/dog.jpg \  
--graph=/oxd553/lightScripts/custom_models/animal_model/output_graph.pb \  
--labels=/oxd553/lightScripts/custom_models/animal_model/output_labels.txt```  
3. Receive your results in the terminal
