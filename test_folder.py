import os

folder_path = "logs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

print(f"Folder created at: {os.path.abspath(folder_path)}")