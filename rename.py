import os

# Paths to the two folders
folder1_path = "Scan_Ana"
folder2_path = "labels_for_retrain_dental"
log_file_path = "renaming_log.txt"

# Get the list of filenames in each folder
folder1_files = sorted(os.listdir(folder1_path))
folder2_files = sorted(os.listdir(folder2_path))

# Create a mapping for new names and log changes
renaming_log = []
name_counter = 0

# Create a mapping for files with the same name in both folders
shared_files = set(folder1_files).intersection(set(folder2_files))
unique_files_folder1 = set(folder1_files) - shared_files
unique_files_folder2 = set(folder2_files) - shared_files

# Function to rename files in a folder
def rename_files(folder_path, files, start_counter):
    counter = start_counter
    for file in files:
        old_path = os.path.join(folder_path, file)
        if os.path.isfile(old_path):
            new_name = f"p_{counter:03d}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            renaming_log.append(f"{new_name} ==> {file}\n")
            counter += 1
    return counter

# Rename shared files with the same name in both folders
for file in shared_files:
    new_name = f"p_{name_counter:03d}"

    # Rename in folder1
    old_path_folder1 = os.path.join(folder1_path, file)
    new_path_folder1 = os.path.join(folder1_path, new_name)
    os.rename(old_path_folder1, new_path_folder1)
    renaming_log.append(f"{new_name} ==> {file}\n")

    # Rename in folder2
    old_path_folder2 = os.path.join(folder2_path, file)
    new_path_folder2 = os.path.join(folder2_path, new_name)
    os.rename(old_path_folder2, new_path_folder2)

    name_counter += 1

# Rename unique files in each folder
name_counter = rename_files(folder1_path, unique_files_folder1, name_counter)
name_counter = rename_files(folder2_path, unique_files_folder2, name_counter)

# Write the renaming log to a file
with open(log_file_path, "w") as log_file:
    log_file.writelines(renaming_log)

print("Renaming completed. Log saved to", log_file_path)
