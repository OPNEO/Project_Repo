'''📦
7. File Organizer (Script)
Topics covered: os, shutil, glob, string ops
Features:
Organizes files in a folder by extension (images, pdfs, docs, etc.)
Move them to separate folders
'''


import os
import shutil

folder_path = r'C:\Users\Sohail\Downloads\test'
list_of_extenstions = set()

if os.path.exists(folder_path):
    for filename in os.listdir(folder_path):
        name, extension = os.path.splitext(filename)
        if extension:  # ignore empty extensions
            list_of_extenstions.add(extension)

for ext in list_of_extenstions:
    folder = os.path.join(folder_path, ext[1:])
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file)
    if os.path.isfile(full_path):
        name, extension = os.path.splitext(file)
        if extension in list_of_extenstions:
            dest_folder = os.path.join(folder_path, extension[1:])
            dest_path = os.path.join(dest_folder, file)
            if not os.path.exists(dest_path):
                shutil.move(full_path, dest_path)
            else:
                print(f"File already exists: {dest_path}")





