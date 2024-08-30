from ultralytics import YOLO

# Load the trained model
model = YOLO("./runs/detect/train2/weights/best.pt")  # Replace with the path to your trained model

# Predict on images in a directory or a single image
results = model.predict(source="./image.png", save=True)  # Replace with your test images directory

# Display results (optional)
for result in results:
    result.show()  # This will display the image with predictions
