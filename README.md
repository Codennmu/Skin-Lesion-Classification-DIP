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
<img width="1167" height="660" alt="scatter plot" src="https://github.com/user-attachments/assets/f49f185a-d8e1-48f7-87f8-9f8cb3b589d3" />


Box Plot:
<img width="861" height="472" alt="boxplot" src="https://github.com/user-attachments/assets/719144c3-a13d-4947-bfd1-5834ed329981" />


Classification Models

Implemented and compared:

Support Vector Machine (SVM) 
Random Forest
K-Nearest Neighbors (KNN)

📊 Results
Model	Accuracy	Result Image
SVM	~85%	<img width="675" height="197" alt="Grid Search" src="https://github.com/user-attachments/assets/bca6bda2-1b8f-48fc-8ebb-daae8fe88c4b" />


Random Forest	~82%	<img width="555" height="217" alt="Random forest" src="https://github.com/user-attachments/assets/c2dd4f35-9f49-4b98-b4d5-719d95eb7f0f" />


KNN	~78%	<img width="461" height="171" alt="KNN report" src="https://github.com/user-attachments/assets/8dfb89ed-8a53-4e5b-b7f0-e090ed362e10" />


Overall Performance:
<img width="733" height="168" alt="overall" src="https://github.com/user-attachments/assets/a5b9df30-db8e-48f0-b3ac-543abfba4a2c" />


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
