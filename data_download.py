import os
import kaggle
import zipfile

# Download dataset from Kaggle
dataset_name = 'ipythonx/wikiart-gangogh-creating-art-gan'
data_dir = './data'

# Ensure the data directory exists
os.makedirs(data_dir, exist_ok=True)

# Download the dataset
kaggle.api.dataset_download_files(dataset_name, path=data_dir, unzip=True)

# Extract any zip files if they exist
for file in os.listdir(data_dir):
    if file.endswith('.zip'):
        with zipfile.ZipFile(os.path.join(data_dir, file), 'r') as zip_ref:
            zip_ref.extractall(data_dir)
