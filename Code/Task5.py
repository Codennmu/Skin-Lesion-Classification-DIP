import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from skimage.feature import hog
from skimage.color import rgb2gray
from sklearn.svm import SVC
import pandas as pd
from tabulate import tabulate

Source_folder = r"D:\MS Documents\3rd Semester\Digital Image Processing\Assignment2 Solution\Data_set"

# Define the paths to your dataset folders for the three classes
melanoma_folder = os.path.join(Source_folder, f'Melanoma')
common_nevus_folder = os.path.join(Source_folder, f'Common Nevus')
atypical_nevus_folder = os.path.join(Source_folder, f'Atypical Nevus')

# Initialize lists to store features and labels
features = []
labels = []

# Define labels for the three classes
class_labels = {
    melanoma_folder: 2,
    common_nevus_folder: 1,
    atypical_nevus_folder: 0
}

# Loop through the class folders and load images
for class_folder, label in class_labels.items():
    for image_filename in os.listdir(class_folder):
        image_path = os.path.join(class_folder, image_filename)
        image = Image.open(image_path)
        image = image.resize((224, 224))  # Resize to a common size if needed
        gray_image = rgb2gray(np.array(image))

        # Compute HOG features
        hog_features = hog(
            gray_image, pixels_per_cell=(16, 16), cells_per_block=(2, 2), orientations=9
        )

        # Store the computed features and corresponding label
        features.append(hog_features)
        labels.append(label)

# Split the data into 80% for training and 20% for testing
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# Grid Search for Hyperparameters
param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1]
}

# Create classifiers
knn_classifier = KNeighborsClassifier()
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
svm_classifier = GridSearchCV(SVC(), param_grid, cv=5)

classifiers = [knn_classifier,
               rf_classifier,
               svm_classifier
               ]

results = []
image_accuracies = []

# Define class names
class_names = {
    0: "Atypical nevus",
    1: "Common nevus",
    2: "Melanoma"
}

for classifier in classifiers:
    # Train the classifier using the training data
    classifier.fit(train_features, train_labels)

    # Use the trained model to make predictions on the test data
    test_predictions = classifier.predict(test_features)

    # Calculate overall accuracy of the solution
    accuracy = accuracy_score(test_labels, test_predictions)
    print(f"Classifier: {classifier.__class__.__name__}")
    print("Overall Accuracy: {:.2f}%".format(accuracy * 100))

    # Calculate accuracy for each image
    image_accuracies = accuracy_score(test_labels, test_predictions)

    # Create a dictionary to store results for this classifier
    result = {
        "Classifier": classifier.__class__.__name__,
        "Overall Accuracy (%)": accuracy * 100,
        "Accuracy Per Image": image_accuracies,
    }

    # Append results to the list
    results.append(result)

    # Generate a classification report with zero_division set to 1
    # report = classification_report(test_labels, test_predictions, target_names=class_labels.keys(), zero_division=1)

    # Generate a classification report
    report = classification_report(
        test_labels, test_predictions, target_names=class_names.values(), zero_division=1)

    print(
        f"Classification Report - {classifier.__class__.__name__}:\n", report)
    print("\n")

# Create a pandas DataFrame from the list of results
results_df = pd.DataFrame(results)

# Print the results as a table using tabulate
results_table = tabulate(results_df, headers='keys',
                         tablefmt='pretty', showindex=False)

# Print the table
print("\nResults:")
print(results_table)
