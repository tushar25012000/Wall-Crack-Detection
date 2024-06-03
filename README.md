# Wall-Crack-Detection-Project

![Screenshot (230)](https://github.com/bhushanbkt/Wall-Crack-Detection-Project/assets/91175596/d3f30927-39ac-4738-8fd2-7050b82d76e7)



This repository contains the code and resources for a Wall Crack Detection project, from data collection to model training and deployment. The project utilizes the Roboflow platform for data preprocessing and the Ultralytics YOLO framework for object detection.

Key Steps:
Data Collection:

Data was collected using Roboflow's core labeling tools for annotating wall crack images.
Model Training:

YOLOv8, implemented using Ultralytics, was used for training the wall crack detection model.
The training process involved fine-tuning on a custom dataset obtained from Roboflow.
Evaluation:

Model performance was evaluated on a validation set to ensure accurate crack detection.
Deployment:

The trained model can be used for real-time crack detection on images or videos.
A simple web application was built using Flask to allow users to upload videos for crack detection.
Project Structure:
data/: Contains the dataset used for training.
yolov8n.yaml: YOLOv8 configuration file.
yolov8n.pt: Pretrained YOLOv8 model.
main.py: Flask application for the web interface.
templates/: HTML templates for the web interface.
static/: Static files including CSS and uploaded videos.
Feel free to explore the code and adapt it to your specific use case!

You can adjust the description based on the specifics of your project, including any additional details or features you'd like to highlight. Once you have this description, you can create a new GitHub repository and add the code and relevant files.





