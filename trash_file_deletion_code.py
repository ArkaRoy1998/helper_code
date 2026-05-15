import os
import shutil

# Target the specific subdirectory where trashed items are stored
my_dir = os.path.expanduser("~/.local/share/Trash/files")

if os.path.exists(my_dir):
    for fname in os.listdir(my_dir):
        # Match names starting with "image"
        if fname.startswith("image"):
            full_path = os.path.join(my_dir, fname)
            
            try:
                if os.path.isdir(full_path) and not os.path.islink(full_path):
                    shutil.rmtree(full_path)  # Deletes folder and all its contents
                else:
                    os.remove(full_path)      # Deletes file or symlink
            except Exception as e:
                print(f"Error deleting {fname}: {e}")
