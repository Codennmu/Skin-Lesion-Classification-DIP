🧠 Skin Lesion Classification using PH2 Dataset

This repository contains a complete end-to-end pipeline for classifying dermoscopic images using Digital Image Processing (DIP) techniques. The project uses the PH2 Dataset to classify skin lesions into three categories:

Common Nevi
Atypical Nevi
Melanoma
📌 Project Overview

The objective of this project is to build a full image analysis workflow—from raw dataset organization to feature extraction and machine learning classification—without using deep learning.

Instead, the focus is on traditional Digital Image Processing techniques covered in the course.

📂 Repository Structure
├── Segregation.py      # Dataset organization based on diagnosis
├── Task1-4.py         # HOG feature extraction + data split + visualization
├── Task5.py           # Model training and evaluation
├── docs/              # Assignment details and final report
├── images/            # Scatter plots, boxplots, GridSearch & model results
🛠️ Methodology
1. Pre-processing & Segregation
Organized raw dataset into three classes
Resized images to 224 × 224
Converted images to grayscale for consistency
2. Feature Extraction
Used Histogram of Oriented Gradients (HOG)
Captures structural and texture-based features
Effective for detecting irregular patterns (important for melanoma)
3. Data Analysis
Used Box Plots and Scatter Plots to analyze feature distribution and class separability

Scatter Plot:
<img width="1167" height="660" alt="scatter plot" src="https://github.com/user-attachments/assets/f7654eae-6437-442a-97ee-45c43ff90b23" />

Box Plot:
<img width="861" height="472" alt="boxplot" src="https://github.com/user-attachments/assets/d1073770-904c-4348-967f-4ae4da12cbe0" />

4. Classification Models

The following machine learning models were implemented and compared:

Support Vector Machine (SVM)
Random Forest
K-Nearest Neighbors (KNN)

GridSearch & Model Evaluation Results:

SVM:
<img width="675" height="197" alt="Grid Search" src="https://github.com/user-attachments/assets/588e529d-d778-40c9-9792-f2443a26a8b2" />

Random Forest:
<img width="555" height="217" alt="Random forest" src="https://github.com/user-attachments/assets/cdaafb85-7d4b-45e7-8ea2-7a91a743a05e" />

K-Nearest Neighbors (KNN):
<img width="461" height="171" alt="KNN report" src="https://github.com/user-attachments/assets/821d669b-4d2a-49a8-a53d-f59cb95b1629" />

Overall Performance:
<img width="733" height="168" alt="overall" src="https://github.com/user-attachments/assets/a9c51111-7c71-4568-aa98-3ebed91028b9" />

⚠️ Note: Results may slightly vary depending on random seed and data split.

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

This project demonstrates the application of Digital Image Processing and Machine Learning in medical image classification.
