import zipfile
import shutil
import os
import time
from datetime import date

# Define the source folder to compress
source_folder = "/Users/michaelhatton/Library/CloudStorage/GoogleDrive-link@arbitraryexecution.com/Shared drives"

# Define the backup folder
backup_folder = "/Users/michaelhatton/backups"

# Get today's date
today = date.today().strftime("%B_%d_%Y")

# Start the timer
start_time = time.time()

# Define the name and path of the compressed file to create
compressed_file_name = f"google_drive_backup_{today}.zip"
compressed_file_path = "temp/" + compressed_file_name

# Start the timer
start_time = time.time()

# Create a zip file object and add the files in the source folder to it
with zipfile.ZipFile(compressed_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = file_path.replace(source_folder, "")
            print(rel_path)
            zip_file.write(file_path, os.path.relpath(file_path, source_folder))

# Copy the compressed file to the destination folder
shutil.copy(compressed_file_path, backup_folder)

# Stop the timer
end_time = time.time()

# Calculate the execution time in seconds
execution_time = end_time - start_time

print(f"Script execution time: {execution_time:.2f} seconds")