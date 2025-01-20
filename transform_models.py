from transformers import AutoTokenizer, ViTModel, BlipProcessor, BlipForConditionalGeneration
from torchvision import transforms
import torch

# Set up device (GPU/CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Set up image transformations
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Initialize models
tokenizer = AutoTokenizer.from_pretrained("google/vit-base-patch16-224-in21k")
vit_model = ViTModel.from_pretrained("google/vit-base-patch16-224-in21k").to(device)
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
