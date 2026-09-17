from pathlib import Path


def organize_files(folder_path):
    """Move files in a folder into subfolders based on extension."""
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    # Your code here
    return "Files organized successfully."


def rename_files(folder_path, prefix):
    """Rename files in a folder by adding a prefix."""
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    # Your code here
    return "Files renamed successfully."


def generate_summary_report(input_file, output_file):
    """Read a task list and create a summary report."""
    source = Path(input_file)
    if not source.exists():
        raise FileNotFoundError(f"File not found: {source}")

    # Your code here
    return "Summary report created successfully."


def main():
    """Run automation options from a simple menu."""
    print("Python Automation Menu")
    print("1. Organize files by extension")
    print("2. Rename files with a prefix")
    print("3. Generate summary report")
    print("4. Exit")

    # Your code here


if __name__ == "__main__":
    main()
