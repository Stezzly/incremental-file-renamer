# Incremental File Renamer

This Python program renames files in a specified directory incrementally, allowing users to organize their files easily. The renamed files will be formatted as `image1`, `image2`, `image3`, and so on, up to a maximum of 50 files. The user can confirm the new names and has the option to revert to the original names if needed.

## Features

- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Incremental Renaming**: Renames files in the specified directory with a simple naming convention.
- **User Confirmation**: Prompts the user to confirm keeping the new file names.
- **Rollback Option**: Allows reverting files back to their original names if the user declines to keep the new names.
- **Batch Processing**: Supports processing multiple files in batches of 50.

## Requirements

- **Python 3.x**: Ensure that Python is installed on your system.
- No additional libraries are required.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Stezzly/incremental-file-renamer.git
   cd incremental-file-renamer
   ```

2. **Run the Script**:
   - You can run the script using Python:
     ```bash
     python incremental_file_renamer.py
     ```

## Usage

1. **Specify the Directory**: When prompted, enter the full path to the directory containing the files you want to rename.
2. **Follow Prompts**: The script will rename the files incrementally and ask for confirmation to keep the new names. If you choose not to keep them, the script will revert the names back to their original state.
3. **Continue Processing**: After confirming the names, you can choose to continue processing the next batch of 50 images.

## Example

```
Enter the path to the directory: /path/to/your/files
Renamed 'old_file1.jpg' to 'image1.jpg'
Renamed 'old_file2.png' to 'image2.png'
...
Are you okay with the updated file names? (Y/N): Y
Would you like to continue processing the next 50 images? (Y/N): N
Exiting the application.
```

## Important Notes

- The script will only rename files and will stop renaming after 50 files per batch.
- Ensure you have backups of your files in case of unintended consequences.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
