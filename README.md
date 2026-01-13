# Transformer Projects Repository

## WHAT IS IT?

This repository is a comprehensive collection of **Vision Transformer (ViT) and other Transformer model applications** across multiple domains including medical imaging, emotion recognition, and computer vision tasks. The repository demonstrates the versatility and effectiveness of transformer architectures for various classification and segmentation problems.

## 🔬 Project Overview

### Medical Image Analysis Projects

#### 🫀 Cardiac Condition Detection
- **PAH Classification** (`pah-vit.ipynb`): Vision Transformer for classifying Pulmonary Atrial Hypertension from echocardiogram images
  - **Dataset**: CardiacNet dataset 
  - **Performance**: 97.36% accuracy with pretrained ViT
  - **Methodology**: A4C (Apical 4-Chamber) heart view slice selection → ViT classification

- **ASD Classification** (`asd-vit.ipynb`): Vision Transformer for detecting Atrial Septal Defect from echocardiogram images
  - **Dataset**: Custom echocardiogram dataset
  - **Methodology**: Similar preprocessing pipeline as PAH classification

#### 🧠 EEG Signal Analysis
- **Emotion Classification** (`EEG-SEED-V/`): Transformer-based emotion recognition from EEG signals
  - **Dataset**: SEED-V dataset (Subject 1, Session 1)
  - **Process**: EEG signals → downsampling (200Hz) → bandpass filtering (1-50Hz) → CWT scalogram images → ViT classification
  - **Features**: 62-channel, 5-band EEG signal processing

#### 🩺 Dermatological Applications
- **Skin Lesion Detection** (`skin_lession_detection.ipynb`): High-accuracy skin lesion classification
- **Skin Lesion Segmentation** (`Segmentation/`): Multiple model comparison for skin lesion segmentation
  - **Models**: UNet, ResNet-based Modified UNet, DeepLabV3+
  - **Performance**: Up to 96% accuracy with DeepLabV3+
  - **Pipeline**: Images → grayscale conversion → watershed algorithm ground truth → segmentation models

### Other Applications

#### 🚬 Behavioral Analysis
- **Smoking Classification** (`smoking-classify-vit (1).ipynb`): ViT-based smoking behavior detection from images

#### 💊 Drug Discovery
- **Transformer for Drug Discovery** (`Drug discovery using transformer model/`): Applying transformer architectures to pharmaceutical research

#### 🔬 General ViT Implementations
- **ViT from Scratch** (`vit-implementation.ipynb`): Custom Vision Transformer implementation
- **Medical Dataset Application** (`vit-on-breastmnist.ipynb`): ViT applied to BreastMNIST dataset
- **Text Generation** (`GPT2_textGen.ipynb`): GPT-2 based text generation
- **Model Interpretability** (`Bert_with_captum.ipynb`): BERT model analysis using Captum

## 🛠️ Supporting Utilities

- **`file_formater.py`**: Automated image file renaming utility for dataset preparation
- **`dataset-prep.ipynb`**: Slice extraction from .nii files (CardiacNet dataset processing)

## 📊 Performance Summary

| Project | Model | Accuracy | Dataset |
|---------|-------|----------|---------|
| PAH Classification | Pretrained ViT | 97.36% | CardiacNet Echocardiograms |
| Skin Lesion Segmentation | DeepLabV3+ | ~96% | Custom Dermatological Images |
| Skin Lesion Detection | Various CNNs | >90% | Dermatological Images |
| EEG Emotion Recognition | ViT on CWT Scalograms | - | SEED-V Dataset |

## 🔄 Typical Workflow

### For Medical Image Classification:
1. **Data Preparation**: CardiacNet dataset → slice selection → best A4C views
2. **Preprocessing**: Image formatting → train/test split
3. **Model Training**: ViT (with/without pretrained weights)
4. **Evaluation**: Performance assessment and validation

### For EEG Analysis:
1. **Signal Processing**: Raw EEG → downsampling → bandpass filtering
2. **Feature Extraction**: 62-channel, 5-band signal separation
3. **Image Generation**: CWT scalogram creation
4. **Classification**: ViT-based emotion recognition

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- PyTorch
- Transformers library
- OpenCV
- NumPy, Pandas
- Jupyter Notebook

### Quick Start
1. Clone the repository
2. Install required dependencies
3. Choose a project notebook
4. Follow the specific README/instructions in each project folder

## 📁 Repository Structure

```
├── pah-vit.ipynb                 # PAH classification
├── asd-vit.ipynb                 # ASD classification  
├── smoking-classify-vit (1).ipynb # Smoking detection
├── skin_lession_detection.ipynb  # Skin lesion detection
├── vit-implementation.ipynb      # Custom ViT implementation
├── vit-on-breastmnist.ipynb     # ViT on medical dataset
├── EEG-SEED-V/                  # EEG emotion recognition
├── Drug discovery using transformer model/ # Pharmaceutical applications
├── Segmentation/                # Skin lesion segmentation
├── file_formater.py            # Utility script
└── dataset-prep.ipynb          # Data preparation
```

## 🎯 Key Features

- **Multi-domain Applications**: Medical imaging, signal processing, computer vision
- **State-of-the-art Models**: Vision Transformers, BERT, GPT-2
- **High Performance**: Achieving >95% accuracy on several tasks
- **Complete Pipelines**: From raw data to trained models
- **Reproducible Research**: Well-documented notebooks and utilities

## 📝 Citation

If you use this repository in your research, please cite the individual projects and datasets used.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

---

*This repository demonstrates the power and versatility of transformer architectures across various domains, particularly in medical imaging and signal processing applications.*
