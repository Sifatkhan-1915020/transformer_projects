import os

# Define folder paths
asd_folder = "ASDimage"
non_asd_folder = "NonASDimage"

# Function to rename files in a folder
def rename_files(folder, label):
    files = sorted(os.listdir(folder))  # Sort files to maintain order
    for i, file in enumerate(files, start=1):
        if file.endswith(".jpg"):  # Ensure it's a .jpg file
            old_path = os.path.join(folder, file)
            new_name = f"{label}_{i:03d}.jpg"  # Format: Label_001.jpg
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")

# Rename files in each folder
rename_files(asd_folder, "ASD")
rename_files(non_asd_folder, "NonASD")

print("Renaming completed.")
