import requests
from bs4 import BeautifulSoup

# URL of the published Google Document
# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub"


def getData(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the first table element
        table = soup.find("table")

        if not table:
            print("No table found in the document.")
            return []

        # Extract all rows from the table, skipping the first row
        rows = table.find_all("tr")[1:]  # Slicing to skip the first row

        # Extract data from rows
        data = [
            [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
            for row in rows
        ]
        return data

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def getGrid():
    # Fetch raw data from the specified URL
    raw_data = getData(url)

    # Check if data was successfully retrieved
    if not raw_data:
        return

    # Initialize variables to track the maximum x and y coordinates
    x_range = 0
    y_range = 0

    # Iterate over each row in the data
    for row in raw_data:
        try:
            # Attempt to parse x and y coordinates as integers from the row data
            x_coords = int(row[0])  # Assuming the first column contains x coordinates
            y_coords = int(row[2])  # Assuming the third column contains y coordinates
        except (ValueError, IndexError) as e:
            # Handle cases where conversion fails or the expected data is missing
            print(f"Error parsing row {row}: {e}")
            continue  # Skip to the next row

        # Update x_range if the current x coordinate is greater
        x_range = max(x_range, x_coords)

        # Update y_range if the current y coordinate is greater
        y_range = max(y_range, y_coords)

    # Print the maximum x and y coordinates found in the data
    return x_range, y_range


def sortArray():
    # Fetch raw data from the specified URL
    raw_data = getData(url)

    # Check if data was successfully retrieved
    if not raw_data:
        return []

    # Initialize an empty list to store sorted rows
    x_coord_sorted_array = []

    # Iterate over each row in the data
    for row in raw_data:
        try:
            # Attempt to parse x and y coordinates as integers from the row data
            x_coords = int(row[0])  # Assuming the first column contains x coordinates
            y_coords = int(row[2])  # Assuming the third column contains y coordinates
        except (ValueError, IndexError) as e:
            # Handle cases where conversion fails or the expected data is missing
            print(f"Error parsing row {row}: {e}")
            continue  # Skip to the next row

        # Append the row to the list along with the extracted x and y coordinates
        x_coord_sorted_array.append((x_coords, y_coords, row))

    # Sort the array first by x_coords and then by y_coords
    x_coord_sorted_array.sort(key=lambda item: (item[0], item[1]))

    # Extract the sorted rows (discard x_coords and y_coords)
    sorted_rows = [item[2] for item in x_coord_sorted_array]

    return sorted_rows


def createsortedGrid(sorted_data, x_range, y_range):
    # Initialize a 2D list (grid) filled with an empty string space " "
    grid = [[" " for _ in range(y_range + 1)] for _ in range(x_range + 1)]

    # Populate the grid with the second item from each row or " " if no coords and symbol
    for row in sorted_data:
        try:
            x_coords = int(row[0])
            y_coords = int(row[2])
            second_item = row[1]
            grid[x_coords][y_coords] = second_item
        except (ValueError, IndexError) as e:
            print(f"Error placing item from row {row} in grid: {e}")

    return grid


def printGrid(sorted_grid, y_range):
    strings_array = []

    for row in sorted_grid:
        string = ""
        for item in row:
            string += str(item)
        string += "\n"
        strings_array.append(string)

    for string in strings_array:
        print(string, end="")


sorted_data = sortArray()
x_range, y_range = getGrid()
sorted_grid = createsortedGrid(sorted_data, x_range, y_range)

printGrid(sorted_grid, y_range)
