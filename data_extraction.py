import os
import zipfile

# Set Kaggle configuration
os.environ["KAGGLE_CONFIG_DIR"] = os.path.expanduser("~/.kaggle")

# Dataset identifier
dataset = "promptcloud/walmart-product-review-dataset"

# Download dataset
os.system(f"kaggle datasets download -d {dataset}")

# Extract dataset
zip_file = "walmart-product-review-dataset.zip"  # Name of the downloaded zip file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall("dataset")  # Extract contents to the 'dataset' folder

print("Dataset downloaded and extracted successfully!")



import pandas as pd

# File path to the extracted dataset
file_path = "dataset/walmart-product-reviews.csv"  # Replace with the actual file name

# Load the dataset into a DataFrame
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())