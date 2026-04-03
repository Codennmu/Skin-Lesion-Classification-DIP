# 🧠 Skin Lesion Classification using PH2 Dataset

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)  
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-green)](https://github.com/your-username/your-repo-name)  

This repository contains a **complete end-to-end pipeline** for classifying dermoscopic images using **Digital Image Processing (DIP)** techniques. The project uses the **PH2 Dataset** to classify skin lesions into three categories:  

- **Common Nevi**  
- **Atypical Nevi**  
- **Melanoma**  

---

## 📌 Table of Contents

1. [Project Overview](#project-overview)  
2. [Repository Structure](#repository-structure)  
3. [Methodology](#methodology)  
   - [Pre-processing & Segregation](#pre-processing--segregation)  
   - [Feature Extraction](#feature-extraction)  
   - [Data Analysis](#data-analysis)  
   - [Classification Models](#classification-models)  
4. [Results](#results)  
5. [How to Run](#how-to-run)  
6. [Requirements](#requirements)  
7. [Documentation](#documentation)  
8. [Acknowledgment](#acknowledgment)  

---

## 📌 Project Overview

This project implements a **full image analysis workflow** from raw dataset organization to feature extraction and machine learning classification—**without using deep learning**.  

The focus is on traditional **Digital Image Processing techniques** learned in the course.

---

## 📂 Repository Structure

```text
Segregation.py      # Dataset organization based on diagnosis
Task1-4.py         # HOG feature extraction + data split + visualization
Task5.py           # Model training and evaluation
docs/              # Assignment details and final report
images/            # Scatter plots, boxplots, GridSearch & model results
🛠️ Methodology
Pre-processing & Segregation
Organized raw dataset into three classes
Resized images to 224 × 224
Converted images to grayscale
Feature Extraction
Used Histogram of Oriented Gradients (HOG)
Captures structural and texture-based features
Helps detect irregular patterns characteristic of melanoma
Data Analysis

Used Box Plots and Scatter Plots to visualize feature distribution and class separability.

Scatter Plot:


Box Plot:


Classification Models

Implemented and compared:

Support Vector Machine (SVM)
Random Forest
K-Nearest Neighbors (KNN)
📊 Results
Model	Accuracy	Result Image
SVM	~85%	

Random Forest	~82%	

KNN	~78%	

Overall Performance:

⚠️ Results may vary slightly depending on the random seed and data split.

🚀 How to Run
1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Requirements
pip install numpy scikit-image scikit-learn pillow matplotlib pandas tabulate
3. Run the Pipeline
# Step 1: Organize dataset (update file paths first)
python Segregation.py

# Step 2: Feature extraction & visualization
python Task1-4.py

# Step 3: Train and evaluate models
python Task5.py
📦 Requirements
Python 3.x
NumPy
Scikit-image
Scikit-learn
Pillow
Matplotlib
Pandas
Tabulate
📘 Documentation

The docs/ folder contains:

Assignment description
Final technical report
⭐ Acknowledgment

This project demonstrates the practical application of Digital Image Processing and Machine Learning in medical image classification.


---

If you want, I can also make a **version with smaller inline images side-by-side and color-coded tables**, so it looks **professional for a GitHub portfolio**.  

Do you want me to do that next?
