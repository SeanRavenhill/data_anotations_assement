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
        return 0, 0  # Return default values if no data is found

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

    return x_range, y_range


def sortArray():
    # Fetch raw data from the specified URL
    raw_data = getData(url)

    # Check if data was successfully retrieved
    if not raw_data:
        return []

    # Initialize an empty list to store sorted rows
    sorted_array = []

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

        # Append the row to the list along with the extracted y and x coordinates
        # Here, we swap y_coords and x_coords to prioritize sorting by y (vertical position)
        # and then by x (horizontal position) if the y coordinates are equal.
        sorted_array.append((y_coords, x_coords, row))

    # Sort the array first by y_coords and then by x_coords
    sorted_array.sort(key=lambda item: (item[0], item[1]))

    # Extract the sorted rows (discard y_coords and x_coords)
    sorted_array = [item[2] for item in sorted_array]

    return sorted_array


def createsortedGrid(sorted_data, x_range, y_range):
    # Initialize a 2D list (grid) filled with an empty string space " "
    grid = [[" " for _ in range(x_range + 1)] for _ in range(y_range + 1)]

    # Populate the grid with the second item from each row
    for row in sorted_data:
        try:
            x_coords = int(row[0])
            y_coords = int(row[2])

            # Ensure coordinates are within grid bounds
            if 0 <= x_coords <= x_range and 0 <= y_coords <= y_range:
                second_item = row[1]
                grid[y_coords][
                    x_coords
                ] = second_item  # Place the item at the correct coordinates
            else:
                print(f"Coordinates ({x_coords}, {y_coords}) are out of bounds.")
        except (ValueError, IndexError) as e:
            print(f"Error placing item from row {row} in grid: {e}")

    return grid


def printGrid(sorted_grid):
    strings_array = []

    # Create string representations of each row in the grid
    for row in sorted_grid:
        string = ""
        for item in row:
            string += str(item)
        string += "\n"  # Add a newline character after each row
        strings_array.append(string)

    # Reverse the array of row strings
    # This is done to adjust the visual representation such that the first row
    # of the data (which might be the "bottom" row in some visualizations) is printed last,
    # aligning the visual output with the expected orientation where the "top" of the data
    # corresponds to the beginning of the output.
    strings_array.reverse()

    # Print each row string
    for string in strings_array:
        print(string, end="")  # Print without adding additional newlines


# Fetch and process the data
sorted_array = sortArray()
x_range, y_range = getGrid()
sorted_grid = createsortedGrid(sorted_array, x_range, y_range)

printGrid(sorted_grid)
