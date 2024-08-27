import os
import random
import shutil
from typing import List, Tuple

def splitDataset(images: List[str], trainRatio: float, validateRatio: float) -> Tuple[List[str], List[str], List[str]]:
    random.shuffle(images)
    totalImages = len(images)
    
    trainEnd = int(trainRatio * totalImages)
    validateEnd = trainEnd + int(validateRatio * totalImages)
    
    trainImages = images[:trainEnd]
    validateImages = images[trainEnd:validateEnd]
    testImages = images[validateEnd:]
    
    return trainImages, validateImages, testImages

def renameImages(directory: str, images: List[str]) -> List[str]:
    renamedImages = []
    for idx, image in enumerate(images):
        newName = f"img_{idx}.jpg"
        oldPath = os.path.join(directory, image)
        newPath = os.path.join(directory, newName)
        os.rename(oldPath, newPath)
        renamedImages.append(newName)
    return renamedImages

def organizeImages(directory: str, trainRatio: float = 0.7, validateRatio: float = 0.15):
    images = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Rename images to a consistent format
    images = renameImages(directory, images)
    
    # Split dataset
    trainImages, validateImages, testImages = splitDataset(images, trainRatio, validateRatio)
    
    # Create subfolders if they don't exist
    trainDir = os.path.join(directory, "train/images")
    validateDir = os.path.join(directory, "validate/images")
    testDir = os.path.join(directory, "test")

    for subdir in [trainDir, validateDir, testDir]:
        if not os.path.exists(subdir):
            os.makedirs(subdir)
    
    # Create empty "labels" subfolders in train and validate
    for subdir in ["train", "validate"]:
        labelsDir = os.path.join(directory, subdir, "labels")
        if not os.path.exists(labelsDir):
            os.makedirs(labelsDir)
    
    # Move the images to the corresponding folders
    for image in trainImages:
        try:
            shutil.move(os.path.join(directory, image), os.path.join(trainDir, image))
        except FileNotFoundError:
            print(f"File not found: {image}. Skipping.")
        
    for image in validateImages:
        try:
            shutil.move(os.path.join(directory, image), os.path.join(validateDir, image))
        except FileNotFoundError:
            print(f"File not found: {image}. Skipping.")
        
    for image in testImages:
        try:
            shutil.move(os.path.join(directory, image), os.path.join(testDir, image))
        except FileNotFoundError:
            print(f"File not found: {image}. Skipping.")
    
    print(f"Organized images into: {len(trainImages)} train, {len(validateImages)} validate, {len(testImages)} test")

def main(query: str = "tiger"):
    directory = f"images/{query}"
    
    # Organize images with 70% for training, 15% for validation, 15% for testing
    organizeImages(directory, trainRatio=0.7, validateRatio=0.15)

if __name__ == "__main__":
    main()
