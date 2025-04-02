# PDF Splitter
A simple yet powerful command-line tool to split PDF files into multiple files based on specified page ranges.

## Features
- Split a PDF into multiple files based on defined page ranges
- Extract individual pages or series of pages
- Automatically organize output files in a clear folder structure
- Simple command-line interface

## Installation
### Prerequisites

Python 3.6 or higher
PyPDF2 library

### Installation Steps

1. Clone this repository or download the `pdf_splitter.py` script
```bash
git clone https://github.com/your-username/pdf-splitter.git
cd pdf-splitter
```

2. Install the required dependencies
```bash
pip install PyPDF2
```

## Usage
The basic syntax is:
```bash
python pdf_splitter.py path/to/file.pdf range1 range2 range3 ...
```

Where:

- `path/to/file.pdf` is the path to the PDF file you want to split
- `range1 range2 range3 ...` are the page ranges to extract

### Page Range Format
Page ranges can be specified in two ways:

An individual page: `5` (extracts only page 5)
A range of pages: `1-5` (extracts pages 1 through 5 inclusive)

### Examples
Extract pages 1 to 5, 10 to 15, and page 20 from a PDF:

python pdf_splitter.py document.pdf 1-5 10-15 20

### Additional Options
`--output` or `-o`: Specify a custom output folder (default: "output")
```bash
python pdf_splitter.py document.pdf 1-5 10-15 --output my_extracts
```

## Output File Structure
The generated PDF files are organized in a two-level folder structure:
```
output_folder/
└── original_filename/
    ├── original_filename_range1.pdf
    ├── original_filename_range2.pdf
    └── ...
```
For example, if you run:
```bash
python pdf_splitter.py report.pdf 1-5 10-15 20
```

You will get:
```
output/
└── report/
    ├── report_1-5.pdf
    ├── report_10-15.pdf
    └── report_20-20.pdf
```
## Known Limitations

- Page numbers start at 1 (as in a normal PDF reader)
- Invalid page ranges (e.g., pages that don't exist in the document) will be ignored with a warning

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
