import os
from random import randrange, uniform
from PIL import Image, ImageEnhance
import numpy as np

def adjustBrightness(image: Image.Image, factor: float) -> Image.Image:
    """Adjust the brightness of an image by a given factor."""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def addNoise(image: Image.Image, noise_level: float) -> Image.Image:
    """Add random noise to an image."""
    np_image = np.array(image)
    noise = np.random.normal(0, noise_level, np_image.shape)
    np_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(np_image)

def processImages(directory: str):
    """Process all images in the specified directory by adjusting brightness and adding noise."""
    noiseLevel: int = 25
    for filename in os.listdir(directory):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)

            distortion = randrange(3)
            match distortion:
                case 1:
                    brightnessFactor: float = uniform(0.5, 1.5)
                    image = adjustBrightness(image, brightnessFactor)
                case 2:
                    image = addNoise(image, noiseLevel)
                case default:
                    continue
            
            # Save the modified image
            modified_image_path = os.path.join(directory, f"{filename}")
            image.save(modified_image_path)
            print(f"Processed {filename} -> {modified_image_path}")

def main(query: str = "tiger"):
    print("Modifying Images")
    directory = f"images/{query}"
    processImages(directory)
    print("Image Modifications Complete!")

if __name__ == "__main__":
    main()