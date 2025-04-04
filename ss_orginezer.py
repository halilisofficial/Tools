import os
import shutil
from PIL import Image
import pytesseract


"""Summary:This Python script processes screenshots in a specified folder, extracts text from images using OCR, categorizes the images based on the extracted text and file names, and moves them to appropriate folders, including specific folders for social media if the file name contains related keywords (e.g., Instagram, Facebook, etc.).
"""

# Folder where screenshots are stored
folder_path = "/storage/emulated/0/Download/test/algorithm questions/ss"

# Keywords for categories
categories = {
    "Invoices": ["fatura", "ödeme", "tutar", "invoice", "payment", "amount"],
    "Social Media": ["instagram", "twitter", "whatsapp", "facebook", "youtube"],
    "Recipes": ["tarif", "malzeme", "pişirme", "recipe", "ingredients", "cooking"],
    "Movie Suggestions": ["film", "movie", "suggestion", "suggested", "recommendation"],
    "Music Suggestions": ["music", "song", "track", "album", "suggestion"]
}

# Function to create a folder if it doesn't exist
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to find the category based on the text
def find_category(text, file_name):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():
                return category

    # If no category is found, check file name for social media keywords
    social_media_keywords = ["instagram", "twitter", "whatsapp", "facebook", "youtube"]
    for keyword in social_media_keywords:
        if keyword.lower() in file_name.lower():
            return "Social Media"
    
    return "Others"

# Process the screenshots
def process_screenshots():
    for file in os.listdir(folder_path):
        if file.endswith((".jpg", ".png")):
            file_path = os.path.join(folder_path, file)
            try:
                image = Image.open(file_path)
                text = pytesseract.image_to_string(image)
                category = find_category(text, file)

                target_folder = os.path.join(folder_path, category)
                create_folder(target_folder)
                shutil.move(file_path, os.path.join(target_folder, file))

                print(f"{file} → {category}")
            except Exception as e:
                print(f"Error: {file} → {e}")

process_screenshots()