# AI Stylist: A Fashion Critique and Styling Assistant

Welcome to the **AI Stylist** repository! This project aims to provide fashion critiques and personalized styling suggestions powered by large language models (LLMs). The system offers clothing configurations based on body type, style preferences, and seasonal trends, helping users to make the most out of their wardrobe.

## Project Overview

The AI Stylist utilizes advanced techniques in fashion understanding and AI to:

- **Provide clothing critiques** based on your existing wardrobe.
- **Generate styling suggestions** tailored to body types and specific trends.
- **Assist in reusing clothes** based on personalized style choices and seasonal trends.

This project uses the power of multimodal transformers and integrates computer vision and language models for fashion insights. The main components include:

- Dataset handling and exploration.
- BLIP-based image captioning and fashion critiques.
- Wardrobe analysis and personalized recommendations.

## Getting Started

To set up the project locally, follow the steps below.

### Prerequisites

You need to have Python 3.8 or higher installed. You can install the necessary dependencies via `requirements.txt`:

```bash
pip install -r requirements.txt
```

File Structure

The project consists of the following files:

    dataset_handling_and_exploration.ipynb: Explore and download the dataset.
    blip_model_and_data_preparation.ipynb: Prepare the model and process data for critique generation.
    ai_stylist.py: Main script to run the AI Stylist and provide suggestions.

Dataset

The dataset used in this project is the Abstract Art Dataset from Kaggle. If you're interested in the fashion dataset, you can also replace it with another dataset of your choice, following the same loading process.

You can download the dataset directly from Kaggle using:

kaggle datasets download -d arthurxavier/abstract-art-dataset

Usage

    Run Dataset Handling and Exploration: This will download the dataset and explore its contents.

jupyter notebook dataset_handling_and_exploration.ipynb

Run BLIP Model and Data Preparation: This notebook handles the loading of the BLIP model, processes images, and generates fashion critiques.

jupyter notebook blip_model_and_data_preparation.ipynb

Run AI Stylist: The main Python script that will provide styling suggestions based on your wardrobe and preferences.

    python ai_stylist.py

Example Output

The AI Stylist will generate outputs such as:

    Fashion critique based on an image of your clothing.
    Styling suggestions for how to wear items based on your personal style and trends.

Contributions

We welcome contributions! If you'd like to help improve the AI Stylist, feel free to open an issue or submit a pull request.
Technologies Used

    Transformers (Hugging Face): For model management.
    PyTorch: For deep learning framework.
    BLIP (Bootstrapping Language-Image Pretraining): For generating image captions and critiques.
    Kaggle API: For accessing and downloading datasets.
    PIL: For image processing.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Thanks to the authors of the BLIP model for their amazing work.
    Special thanks to the Kaggle community for their dataset resources.
