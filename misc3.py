import os
import time
import zipfile

while True:
    # Check if a file named "flag.zip" exists
    if os.path.exists("flag.zip"):
        print("Found 'flag.zip'. Stopping the script.")
        break

    # Query the current directory for zip files
    zip_files = [file for file in os.listdir(".") if file.endswith(".zip")]

    if zip_files:
        zip_file = zip_files[0]
        print(f"Processing {zip_file}...")

        # Unzip the zip file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall()

        # Delete the first zip file and keep the others
        os.remove(zip_file)

        print(f"Deleted {zip_file}.")
    else:
        print("No zip files found in the directory!")
        break

    # Sleep for a while (0.5 seconds in this case)
    time.sleep(0.5)