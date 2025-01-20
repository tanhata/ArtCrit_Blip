import os
import json
from model_utils import load_blip_model, generate_captions_batch
from data_utils import get_image_paths, create_data_loader

def generate_captions_for_images(image_folder, output_file):
    """
    Generate captions for all images in the provided folder and save to a file.
    """
    # Load the model and processor
    processor, model = load_blip_model()

    # Get the paths to the images
    image_paths = get_image_paths(image_folder)

    # Generate captions in batches
    captions = generate_captions_batch(image_paths, processor, model)
    
    # Save captions to a JSON file
    results = {image_paths[i]: captions[i] for i in range(len(image_paths))}
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

    print(f"Captions generated and saved to {output_file}")

if __name__ == "__main__":
    image_folder = "./data/raw_images"  # Path to your image directory
    output_file = "captions.json"  # Output file where captions will be saved
    generate_captions_for_images(image_folder, output_file)
