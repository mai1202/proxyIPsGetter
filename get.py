import requests
import zipfile
import os
import requests


zip_url = "https://zip.baipiao.eu.org/"
ports = ["80", "443"]

def download_and_extract():
    # Step 1: Download the zip file
    response = requests.get(zip_url)
    zip_file_path = "download.zip"

    with open(zip_file_path, "wb") as file:
        file.write(response.content)

    # Step 2: Extract the files from the zip
    extracted_files_dir = "./extracted_files/"
    os.makedirs(extracted_files_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extracted_files_dir)

    # Step 3: Combine the text files into one file
    combined_file_path = "ips.txt"

    with open(combined_file_path, "w") as combined_file:
        for root, dirs, files in os.walk(extracted_files_dir):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    for i in ports:
                        if '-'+i+'.' in file:
                            with open(file_path, "r") as txt_file:
                                combined_file.write(txt_file.read())
                        
download_and_extract()
