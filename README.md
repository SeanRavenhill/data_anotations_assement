# Data Annotation Coding Assessment

This project was developed as part of an assessment for **Data Annotation**. The task was to build a Python program that fetches a table from a provided URL and uses the data to programmatically print a secret message in the console by arranging specific characters along a matrix grid.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
- [Assumptions](#assumptions)
- [Technologies Used](#technologies-used)
- [Improvements](#improvements)

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   git clone <repository_url>
   ```
2. Navigate into the project directory.
   ```bash
   cd project-directory
   ```
3. Install the required dependencies (use `pip`).
   ```bash
   pip install -r requirements.txt
   ```
   The key dependencies for this project are:
   - `requests`
   - `beautifulsoup4`

## Usage

After installing the necessary dependencies, run the script to fetch the data, process it, and print the matrix to the console. 

```bash
python script.py
```

Upon running the script, the program will:
1. Fetch data from a URL containing a table.
2. Sort the table data based on specified `x` and `y` coordinates.
3. Place the characters in a grid according to their coordinates.
4. Print a visual representation of the grid, revealing a secret message.

## Project Details

The input data is structured as a table with three columns:
- `x-coordinate`: The horizontal position on the grid.
- `Character`: The character that will be placed at the coordinates.
- `y-coordinate`: The vertical position on the grid.

The program performs the following steps:

1. **Data Extraction:** Using `requests` and `BeautifulSoup`, the script fetches the HTML from the provided URL and extracts the relevant table.
2. **Data Parsing:** The table is parsed, and the characters are placed in a 2D grid according to the coordinates specified in the table.
3. **Grid Population:** The grid is filled with characters, and empty spaces are left as " " (space).
4. **Message Output:** The final message is printed to the console.

## Assumptions

- The table contains three columns, and the first row is a header that is skipped during processing.
- The characters are represented as either solid blocks (█) or shaded blocks (▒) in the table.
- The grid is created based on the maximum `x` and `y` coordinates in the table data.

## Technologies Used

- **Python 3.9+**
- **BeautifulSoup4** for HTML parsing
- **Requests** for making HTTP requests

## Improvements

Some improvements that could be made to the project:
- **Error Handling:** Currently, the program only prints errors. More robust error-handling techniques, such as logging, could be added.
- **Dynamic URL Input:** Allow users to pass a custom URL for data fetching rather than hardcoding it in the script.
- **Unit Testing:** Add tests for individual components, such as data extraction and grid generation, using a testing framework like `pytest`.
