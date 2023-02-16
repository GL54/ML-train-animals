import os
import csv
import shutil

# Set the directory where the images are located
image_directory = "images"

# Set the directory where you want to move the images to
output_directory = "output"

# Read the CSV file and loop over the rows
with open("train.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract the gleason_score from the row
        gleason_score = row["gleason_score"]

        # If the gleason_score is negative or 0+0, use "0" as the folder name
        if gleason_score in ["negative", "0+0"]:
            folder_name = "0"
        else:
            folder_name = gleason_score

        # Construct the destination directory path
        destination_directory = os.path.join(output_directory, folder_name)

        # Create the destination directory if it doesn't already exist
        if not os.path.exists(destination_directory):
            os.mkdir(destination_directory)

        # Construct the path to the image file
        image_filename = row["image_id"] + ".tiff"
        image_path = os.path.join(image_directory, image_filename)

        # Check if the image file exists
        if not os.path.exists(image_path):
            print(f"Image {image_filename} is not available.")
        else:
            # Move the image file to the destination directory
            shutil.move(image_path, destination_directory)
