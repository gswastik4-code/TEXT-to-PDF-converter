Overview

The Python PDF Utility Script (pdf convertor.py) is a lightweight, command-line application developed to streamline common PDF document handling tasks. It provides a simple, efficient, and programmatically controlled method for generating new documents, combining existing files, and optimizing file size through structural rewrite , all directly from the terminal.


Features
Converts user-provided title and body text into a new, single-page PDF document.



Merges new content (text converted to a temporary PDF) with an existing PDF file, prepending the new content to the front.



Reduces the file size of an existing PDF by rewriting its content and structure, ensuring maximum compatibility across pypdf versions.

Technologies/Tools Used

This script relies entirely on the Python environment and the following third-party libraries:

Python 3.x: The core programming language.

fpdf2 (as fpdf): Used specifically for programmatically generating new PDF files from text.

pypdf: Used for manipulating existing PDF structures (reading, writing, merging, and optimization).

Steps to Install & Run the Project

1. Installation

You must have Python installed. Then, install the required libraries:

pip install fpdf2 pypdf


2. Running the Script

Save the provided code as pdf_utility.py.

Open your terminal or command prompt in the directory where you saved the file.

Execute the script:

python pdf_utility.py


Follow the on-screen menu prompts (1, 2, or 3) to choose an operation.

3. Usage Examples

When running the script, you will be prompted for inputs:

Choice 1 (New PDF): Provide a filename, title, and body text.

Choice 2 (Edit/Merge): You will be prompted to create the NEW content first, and then specify the name of the EXISTING PDF and the desired FINAL merged filename.

Choice 3 (Optimize/Compress): Provide the name of the existing PDF you wish to optimize. The output file will have _compressed appended to its name.

Instructions for Testing

Testing relies on Manual and Unit Verification of the resulting files:

Manual Verification (System Testing): Run each of the three functions (Create, Merge, Optimize) and verify the resulting PDF file using a standard PDF reader (e.g., Adobe Acrobat, browser PDF viewer). Check the content, page order, and file size (expecting slight reduction for optimization).

Unit Verification (Input Handling): Test the script by intentionally providing incorrect file paths (e.g., trying to optimize a non-existent file) or entering letters instead of numbers in the menu to ensure the error handling is robust.

Screenshots (CLI)

The user experience is text-based:

--- PDF Utility Menu ---

1 for new pdf
2 for edit existing pdf by adding new topic
3 for compressing Pdf
Enter choice (1-3): 3
Compressing PDF name (e.g., large_file): huge_report.pdf
[SUCCESS] Pdf is successfully compressed as: huge_report_compressed.pdf
