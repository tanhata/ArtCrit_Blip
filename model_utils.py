import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

def load_blip_model():
    """
    Load the BLIP model for image captioning.
    """
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def generate_caption(image_path, processor, model):
    """
    Generate a caption for an image using the BLIP model.
    """
    # Load and preprocess the image
    image = Image.open(image_path).convert('RGB')

    # Prepare the inputs for the model
    inputs = processor(images=image, return_tensors="pt")

    # Generate the caption
    out = model.generate(**inputs)
    
    # Decode and return the caption
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def generate_captions_batch(image_paths, processor, model):
    """
    Generate captions for a batch of images.
    """
    captions = []
    for image_path in image_paths:
        caption = generate_caption(image_path, processor, model)
        captions.append(caption)
    return captions
