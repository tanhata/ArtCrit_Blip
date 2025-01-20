# Art Critic: AI Art Critique Powered by BLIP

Welcome to the **Art Critic** repository! This project uses the **BLIP (Bootstrapping Language-Image Pretraining)** model to critique and provide in-depth analysis of art pieces. The AI is fine-tuned to interpret art based on visual features and generate insightful critiques about artistic style, composition, and thematic content.

## Project Overview

The **Art Critic** system uses advanced AI to:

- **Critique artwork** based on its visual features, style, and composition.
- **Generate in-depth analysis** about various aspects of the artwork (e.g., color usage, technique, symbolism).
- **Provide artist-specific feedback** by analyzing styles from different art movements and artists.

The model is fine-tuned on a dataset of artwork images to generate meaningful critiques of the art, similar to how a human art critic would evaluate pieces.

### Key Features:

- **Image-based analysis**: Generate critiques by processing artwork images.
- **Fine-tuned BLIP model**: Pre-trained on various art datasets, the BLIP model interprets visual cues to provide insightful commentary.
- **Personalized feedback**: The model can be adapted to focus on specific artistic movements or time periods.

## Getting Started

To set up the project locally, follow the steps below.

### Prerequisites

Make sure you have Python 3.8 or higher installed. You can install the necessary dependencies via the `requirements.txt`:

```bash
pip install -r requirements.txt
```
### File Structure

The project consists of the following files:

    art_dataset_handling_and_exploration.ipynb: Explore and download art datasets.
    blip_model_and_finetuning.ipynb: Fine-tune the BLIP model for art critique generation.
    art_critic.py: Main script to run the Art Critic and provide detailed analysis of artworks.

### Dataset

The project uses the Van Gogh Dataset (or any other suitable art dataset) for training and fine-tuning the BLIP model. The dataset includes various artwork images along with metadata, which allows the model to learn specific patterns and critique the art accurately.

You can download a sample dataset from a source like Kaggle or other art repositories. Modify the code to use your dataset of choice.

kaggle datasets download -d user/van-gogh-dataset

### Usage

    Run Dataset Handling and Exploration: This will download and explore the art dataset.

```art_dataset_handling_and_exploration.ipynb```

Fine-tune the BLIP Model: This notebook fine-tunes the BLIP model using the art dataset for generating artwork critiques.

``` blip_model_and_finetuning.ipynb```

Run Art Critic: The main Python script provides critiques of artwork images based on the trained model.

    python art_critic.py

### Example Output

The Art Critic will generate outputs like:

    Detailed critiques of the artwork.
    Analysis of artistic elements such as brush strokes, color balance, and symbolism.
    Insights into the artist's style based on the visual and thematic features of the artwork.

### Contributions

Contributions are welcome! If you'd like to improve the Art Critic, please open an issue or submit a pull request.

### Technologies Used

    BLIP (Bootstrapping Language-Image Pretraining): Pre-trained model for generating image captions and critiques.
    PyTorch: Deep learning framework for model training and inference.
    Transformers (Hugging Face): For managing pre-trained models and model fine-tuning.
    Kaggle API: To access and download datasets.
    PIL: For image processing.

### License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Thanks to the BLIP model authors for their contributions.
    Special thanks to the Kaggle community for their open art datasets.
