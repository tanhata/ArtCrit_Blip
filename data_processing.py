import os
from PIL import Image

# Assuming data is extracted in './data/wikiart-gangogh-creating-art-gan/'
dataset_folder = './data/wikiart-gangogh-creating-art-gan/'

image_paths = []
labels = []

for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            image_paths.append(os.path.join(root, file))
            # Extract label based on directory structure or filename
            labels.append(root.split("/")[-1])  # For example: the folder name as the label

print(f"Found {len(image_paths)} images.")
