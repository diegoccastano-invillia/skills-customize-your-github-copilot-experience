# 📘 Assignment: Python Automation

## 🎯 Objective

Practice reading and writing files, organizing data, and automating repetitive tasks in Python using the standard library. Students will build small scripts that process folders, rename files, and generate summaries from text content.

## 📝 Tasks

### 🛠️ Organize Files by Extension

#### Descrição
Write a script that receives a folder path and automatically groups all files into subfolders based on their extensions.

#### Requisitos
O programa concluído deve:

- Ask the user for a folder path.
- Create a folder for each file extension found in that directory.
- Move each file into its matching folder.
- Keep the original file name unchanged.
- Print a summary showing how many files were moved.
- Handle folders that do not exist by showing a helpful error message.

### 🛠️ Rename Files in Bulk

#### Descrição
Build a function that renames every file in a folder by adding a custom prefix while preserving the original extension.

#### Requisitos
O programa concluído deve:

- Accept a folder path and a prefix as input.
- Rename every file in that folder, excluding subdirectories.
- Preserve each file's extension.
- Avoid renaming files that already have the chosen prefix.
- Print a list of the old and new names.

### 🛠️ Create a Daily Summary Report

#### Descrição
Read a text file with a list of tasks and generate a short summary report with totals and insights.

#### Requisitos
O programa concluído deve:

- Read a file containing one task per line.
- Count how many tasks are in the file.
- Count how many words are in the file total.
- Identify the most common words, ignoring case and basic punctuation.
- Save the summary to a new report file.
- Print the saved summary path for the user.

### 🛠️ Bonus Challenge

#### Descrição
Add a small menu system so the user can choose which automation task to run.

#### Requisitos
O programa concluído deve:

- Show a menu with the available automation options.
- Run the selected function based on user input.
- Keep the program running until the user chooses to exit.
- Use functions to keep the code organized and easy to read.
