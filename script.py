import os

def rename_readme_files():
    for dirpath, dirnames, filenames in os.walk("."):  # Use "." to refer to the current directory
        for filename in filenames:
            if filename == "README.txt":
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, "README.md")
                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} to {new_file}")

# Call the function
rename_readme_files()
