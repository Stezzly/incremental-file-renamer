import os
import shutil

def rename_files_in_directory(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
        return

    # Counter for new file names
    counter = 1
    # Store original file names
    original_names = {}
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

            # Store the original name for potential rollback
            original_names[counter] = filename

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

    # Ask the user for confirmation to keep the new names
    confirm = input("Are you okay with the updated file names? (Y/N): ").strip().upper()
    
    if confirm == 'Y':
        print("The new file names have been kept.")
    else:
        # Rename back to original names
        print("Reverting to original file names...")
        for i in range(1, counter):
            original_name = original_names[i]
            newname = f"{prefix}{i}{os.path.splitext(original_name)[1]}"
            os.rename(os.path.join(directory, newname), os.path.join(directory, original_name))
            print(f"Renamed '{newname}' back to '{original_name}'")
        print("Reverted to original file names.")

    # Ask if the user wants to continue processing the next 50 images
    continue_processing = input("Would you like to continue processing the next 50 images? (Y/N): ").strip().upper()
    if continue_processing == 'Y':
        rename_files_in_directory(directory)  # Recursively call the function for next batch
    else:
        print("Exiting the application.")

if __name__ == "__main__":
    # Ask the user for the directory
    directory = input("Enter the path to the directory: ")
    rename_files_in_directory(directory)
