from ultralytics import YOLO
import os

query = "tiger"
# Define the target directory
project_dir = f"runs/detect/{query}"
# Create the directory if it doesn't exist
os.makedirs(project_dir, exist_ok=True)

# Load a model
model = YOLO("yolov8s.yaml")  # build a new model from scratch
#model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="config.yaml", epochs=100, project=f"/runs/detect/{query}", name=f"{query}_model")  # train the model
metrics = model.val()  # evaluate model performance on the validation set
path = model.export(format="onnx")  # export the model to ONNX format