import os
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms

class FashionDataset(Dataset):
    """
    Custom dataset for loading and preprocessing images.
    """
    def __init__(self, image_paths, transform=None):
        self.image_paths = image_paths
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image = Image.open(image_path).convert("RGB")
        
        if self.transform:
            image = self.transform(image)

        return image

def get_image_paths(data_dir):
    """
    Retrieve image file paths from a directory.
    """
    image_paths = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(('jpg', 'jpeg', 'png')):
                image_paths.append(os.path.join(root, file))
    return image_paths

def create_data_loader(image_paths, batch_size=16, shuffle=True):
    """
    Create a DataLoader for the images.
    """
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    dataset = FashionDataset(image_paths, transform)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    
    return data_loader
