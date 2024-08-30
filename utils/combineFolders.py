import os
import shutil

def mergeFolders(src1: str, src2: str, dest: str):
    """Merges two query folders into a single folder with combined train, validate, and test subfolders, ensuring unique filenames."""
    
    # Define the subfolders to merge
    subfolders = ['train/images', 'train/labels', 'validate/images', 'validate/labels', 'test']
    
    # Initialize a counter for unique filenames
    counter = 1
    
    # Initialize counters for each category
    train_count = 0
    validate_count = 0
    test_count = 0
    
    for subfolder in subfolders:
        # Create destination subfolder if it doesn't exist
        destSubfolder = os.path.join(dest, subfolder)
        if not os.path.exists(destSubfolder):
            os.makedirs(destSubfolder)
        
        # Determine category based on subfolder name
        if 'train' in subfolder:
            category = 'train'
        elif 'validate' in subfolder:
            category = 'validate'
        else:
            category = 'test'
        
        # Merge files from src1
        src1Subfolder = os.path.join(src1, subfolder)
        for filename in os.listdir(src1Subfolder):
            srcFile = os.path.join(src1Subfolder, filename)
            base, extension = os.path.splitext(filename)
            destFile = os.path.join(destSubfolder, f"img_{counter}{extension}")
            shutil.copy(srcFile, destFile)
            counter += 1
            
            # Update category count
            if category == 'train':
                train_count += 1
            elif category == 'validate':
                validate_count += 1
            elif category == 'test':
                test_count += 1
        
        # Merge files from src2
        src2Subfolder = os.path.join(src2, subfolder)
        for filename in os.listdir(src2Subfolder):
            srcFile = os.path.join(src2Subfolder, filename)
            base, extension = os.path.splitext(filename)
            destFile = os.path.join(destSubfolder, f"img_{counter}{extension}")
            shutil.copy(srcFile, destFile)
            counter += 1
            
            # Update category count
            if category == 'train':
                train_count += 1
            elif category == 'validate':
                validate_count += 1
            elif category == 'test':
                test_count += 1

    print(f"Folders {src1} and {src2} merged into {dest} with unique filenames.")
    print(f"Organized images into: {train_count} train, {validate_count} validate, {test_count} test")

def main():
    # Example usage:
    query1 = "scrabble-tiles"
    query2 = "street-signs-real"
    destination = "letters"
    
    src1 = f"images/{query1}"
    src2 = f"images/{query2}"
    dest = f"images/{destination}"
    
    mergeFolders(src1, src2, dest)

if __name__ == "__main__":
    main()
