import os

def create_folders(parent_folder, folder_names):
    # Combine the parent folder path with each folder name
    folder_paths = [os.path.join(parent_folder, folder) for folder in folder_names]

    # Create folders
    for folder_path in folder_paths:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder created: {folder_path}")

if __name__ == "__main__":
    # Specify the parent folder path
    parent_folder = r"C:\Users\attha\OneDrive\Documents\mydoc\Personal Data Projects\CS50\folder maker"  # Replace with the actual path



    # Specify the folder names
    folder_names = ["Week 0 - Scratch", "Week 1 - C", "Week 2 - Arrays", "Week 3 - Algorithms", "Week 4 - Memory", "Week 5 - Data Structures",
                    "Week 6 - Python", "Week 7 - SQL", "Week 8 - HTML, CSS, JavaScript", "Week 9 - Flask", "Week 10 - Emoji"]

    # Create folders
    create_folders(parent_folder, folder_names)

