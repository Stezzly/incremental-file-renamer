import os

def rename_files_in_directory(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
        return

    # Counter for new file names
    counter = 1

    # Specified prefix for the new file names
    prefix = "image"

    # Loop through the files in the directory
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)

        # Ensure it's a file
        if os.path.isfile(file_path):
            # Get the file extension
            ext = os.path.splitext(filename)[1]
            # Form the new file name
            newname = f"{prefix}{counter}{ext}"

            # Check if the new file name already exists
            if os.path.exists(os.path.join(directory, newname)):
                print(f"Warning: '{newname}' already exists. Skipping '{filename}'.")
                counter += 1
                continue

            # Rename the file
            os.rename(file_path, os.path.join(directory, newname))
            print(f"Renamed '{filename}' to '{newname}'")

            # Increment the counter
            counter += 1

            # Stop renaming after 50 files
            if counter > 50:
                break

    print("Renaming completed from image1 to image50.")

if __name__ == "__main__":
    # Ask the user for the directory
    directory = input("Enter the path to the directory: ")
    rename_files_in_directory(directory)
