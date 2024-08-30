import os
from utils.webScraper import main as webScraperMain
from utils.imageDistortion import main as imageDistortionMain
from utils.organizeImages import main as organizeImagesMain

def createPredefinedClassesFile(classes: list, output_dir: str):
    """Creates a predefined_classes.txt file for LabelImg."""
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the path to the predefined_classes.txt file
    file_path = os.path.join(output_dir, 'predefined_classes.txt')
    
    # Write the classes to the file
    with open(file_path, 'w') as file:
        for cls in classes:
            file.write(f"{cls}\n")
    
    print(f"Predefined classes file created at: {file_path}")

def main():
    query = "letter a"
    query = query.replace(" ", "-")
    numImages = 300
    print("Running webScraper...")
    webScraperMain(query, numImages)
    print("Running imageDistortion...")
    imageDistortionMain(query)
    print("Running organizeImages...")
    organizeImagesMain(query)

    # Define your classes
    classes = ["a"]
    output_dir = f"./images/{query}"
    # Create the predefined_classes.txt file
    createPredefinedClassesFile(classes, output_dir)

if __name__ == "__main__":
    main()