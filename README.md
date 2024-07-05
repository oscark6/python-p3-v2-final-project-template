# Electronics Inventory Management CLI

This project is a Command-Line Interface (CLI) application for managing an inventory of electronic items using SQLite for database management. The CLI allows users to add, list, find, update, and delete electronic items along with their features.

## Features

- **Add Electronic Item**: Add a new electronic item to the inventory.
- **List Electronic Items**: Display a list of all electronic items in the inventory.
- **Find Electronic Item by Name**: Search for an electronic item by its name.
- **Update Electronic Item**: Update details of an existing electronic item.
- **Delete Electronic Item**: Remove an electronic item from the inventory.

## Installation

1. Clone the repository:
    git clone https://github.com/oscark6/electronics-inventory-cli.git
    cd electronics-inventory-cli

2. Set up a virtual environment (optional but recommended):
  pipenv install
pipenv shell
    

3. Install the required dependencies:
  
    pip install click
  

## Usage

1. Initialize the database:
   
    python cli.py
   

2. Run the CLI application:
   
    python cli.py menu
   

3. Follow the on-screen prompts to interact with the inventory management system.

## Code Structure

- **cli.py**: The main CLI application file using the `click` library.
- **helpers.py**: Helper functions for interacting with the SQLite database.
- **models.py**: (Optional) Classes representing the electronic items and their features.

## Example

Here's a quick example of how to use the CLI:

1. Start the application:
   
    python cli.py menu
   

2. Select an option from the menu:
  
    Please select an option:
    1. Add a new electronic item
    2. List all electronic items
    3. Find electronic items by name
    4. Delete an electronic item
    5. Update an electronic item
    0. Exit
    

3. Follow the prompts to add, list, find, delete, or update electronic items.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!



