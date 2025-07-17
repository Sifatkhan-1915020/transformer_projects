# Project Index

## Quick Reference Guide - WHAT IS IT?

This document provides a quick reference to understand what each file/folder in this repository contains.

## 📊 Project Performance Overview

| Project | File | Model Type | Accuracy | Use Case |
|---------|------|------------|----------|----------|
| PAH Detection | `pah-vit.ipynb` | Pretrained ViT | 97.36% | Medical: Heart condition diagnosis |
| ASD Detection | `asd-vit.ipynb` | Vision Transformer | - | Medical: Heart defect detection |
| Skin Segmentation | `Segmentation/` | DeepLabV3+ | ~96% | Medical: Dermatology |
| Skin Detection | `skin_lession_detection.ipynb` | Various CNNs | >90% | Medical: Skin lesion classification |
| EEG Emotion | `EEG-SEED-V/` | ViT on Scalograms | - | Neuroscience: Emotion recognition |
| Smoking Detection | `smoking-classify-vit (1).ipynb` | Vision Transformer | - | Behavioral: Smoking classification |
| Drug Discovery | `Drug discovery using transformer model/` | Transformer | - | Pharmaceutical: Drug research |

## 📁 Detailed File Descriptions

### 🏥 Medical Applications
- **`pah-vit.ipynb`** - Pulmonary Atrial Hypertension detection from echocardiograms using Vision Transformer
- **`asd-vit.ipynb`** - Atrial Septal Defect classification from cardiac images
- **`skin_lession_detection.ipynb`** - Automated skin lesion detection and classification
- **`vit-on-breastmnist.ipynb`** - ViT applied to breast cancer detection dataset

### 🧠 Signal Processing & Neuroscience
- **`EEG-SEED-V/`** - Complete EEG emotion recognition pipeline:
  - `dataprocessor.ipynb` - EEG signal preprocessing and CWT scalogram generation
  - `eeg-seedv-s1s1.ipynb` - ViT-based emotion classification
  - `Readme.txt` - Detailed workflow explanation

### 🎨 Computer Vision & AI
- **`vit-implementation.ipynb`** - Vision Transformer implementation from scratch
- **`smoking-classify-vit (1).ipynb`** - Smoking behavior detection using ViT
- **`Bert_with_captum.ipynb`** - BERT model interpretability using Captum
- **`GPT2_textGen.ipynb`** - Text generation using GPT-2

### 🏗️ Image Segmentation
- **`Segmentation/`** - Advanced skin lesion segmentation:
  - Multiple model comparisons (UNet, Modified UNet, DeepLabV3+)
  - Watershed algorithm for ground truth generation
  - High-accuracy segmentation results (96%+)

### 💊 Pharmaceutical Research
- **`Drug discovery using transformer model/`** - Transformer applications in drug discovery:
  - `notebooke934247046.ipynb` - Main implementation
  - `my_dataframe (1).csv` - Research data

### 🛠️ Utilities & Data Processing
- **`file_formater.py`** - Image file renaming utility for ML datasets
- **`dataset-prep.ipynb`** - Medical image slice extraction from .nii files
- **`EchoDataset_ASD.zip`** - Echocardiogram dataset for ASD classification
- **`meow.ipynb`** - Additional experimental notebook

## 🔄 Typical Usage Patterns

### For Researchers
1. **Medical Imaging**: Start with `pah-vit.ipynb` or `asd-vit.ipynb` for cardiac applications
2. **Dermatology**: Use `skin_lession_detection.ipynb` and `Segmentation/` folder
3. **Neuroscience**: Explore `EEG-SEED-V/` for emotion recognition

### For Developers
1. **Learning ViT**: Begin with `vit-implementation.ipynb`
2. **Pretrained Models**: Check `pah-vit.ipynb` for best practices
3. **Data Processing**: Use `file_formater.py` and `dataset-prep.ipynb`

### For Students
1. **Start Here**: `README.md` for overview
2. **Basic Implementation**: `vit-implementation.ipynb`
3. **Real Applications**: Medical imaging notebooks

## 🎯 Key Insights

### What Makes This Repository Special?
- **High Performance**: Multiple projects achieving >95% accuracy
- **Diverse Applications**: Medical, behavioral, pharmaceutical domains
- **Complete Pipelines**: End-to-end implementations from data to results
- **Educational Value**: Both theoretical implementations and practical applications
- **Research Quality**: Publication-ready results and methodologies

### Why Transformers?
This repository demonstrates that Vision Transformers and other transformer architectures are not just for NLP - they excel at:
- Medical image analysis
- Signal processing (EEG → images)
- Complex pattern recognition
- Multi-modal learning

---

*This index provides a clear answer to "WHAT IS IT?" - a comprehensive showcase of transformer model applications across multiple high-impact domains.*