<h1 align="center">YOLO Training Suite</h1>
<div align="center">
  
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  
</div>

<h2>Description</h2>
<p> 
  This project is a comprehensive solution for object detection training using YOLOv5, providing tools 
  for image collection, annotation, and model training, all in one place.
</p> 
  
<h2>Components</h2> 

<h3>Web Scraper/Data Collection</h3>

The ```webScraper.py``` file uses BeautifulSoup and the "icrawler" library to collect images from Google, Bing, 
and Unsplash. Users can specify a query and the maximum number of images to retrieve from each source. 
The program renames the images consistently and organizes them into a new folder within the "images" 
directory.

Once images are collected, the ```imageDistortion.py``` file applies optional changes to the brightness (increase
or decrease) or adds salt-and-pepper noise. This variation enhances the model's training by exposing it to
images with different qualities and lighting, resulting in a more versatile model.

The ```organizeImages.py``` file creates three folders: "test," "train," and "validate," distributing the images
with 70% for training, 15% for validation, and 15% for testing. It also creates "image" and "label" 
subfolders within the "train" and "validate" folders, preparing them for YOLO in the correct format.

<h3>Annotation</h3>

Using the "labelimg" annotation tool, all images in a specified folder can be annotated easily, with the 
labels saved in the respective "label" folder. The tool also generates a "classes.txt" file, which YOLO 
uses later to identify the classes for training.

<h3>Model Training</h3>

The ```yolo.py``` file, powered by YOLOv5, references the config.yaml file to locate images, labels, and class lists. 
The model size (which affects performance and training time) and the number of epochs (training cycles) are
specified before training begins. The trained model and its performance metrics are exported in ONYX format.

<h3>Model Testing</h3>

The ```testModel.py``` file allows users to test the model on images. The model path is defined, and the program uses 
"image.png" in the root directory to detect objects, displaying the image with any detected bounding boxes.


