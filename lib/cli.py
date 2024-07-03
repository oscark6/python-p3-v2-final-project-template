from helpers import (
    add_electronic,
    get_all_electronics,
    delete_electronic,
    update_electronic,
    add_feature,
    get_features_for_electronic,
    execute_query
)

def main_menu():
    """Display main menu"""
    while True:
        print("\nPlease select an option:")
        print("1. Add a new electronic item")
        print("2. List all electronic items")
        print("3. Find electronic items by tag")
        print("4. Delete an electronic item")
        print("5. Update an electronic item")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting program. Goodbye!")
            break
        elif choice == '1':
            add_electronic_item()
        elif choice == '2':
            list_electronics()
        elif choice == '3':
            find_electronics()
        elif choice == '4':
            delete_electronic_item()
        elif choice == '5':
            update_electronic_item()
        else:
            print("Invalid choice. Please select a valid option.")

def add_electronic_item():
    """Add a new electronic item"""
    name = input("Name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))

    add_electronic(name, brand, price)
    electronic_id = execute_query("SELECT last_insert_rowid()", fetchone=True)[0]

    print(f"Added electronic item: {name} (ID: {electronic_id})")

    add_features(electronic_id)

def add_features(electronic_id):
    """Add features for an electronic item"""
    while True:
        feature_name = input("Enter feature name (leave blank to finish): ")
        if not feature_name:
            break
        add_feature(electronic_id, feature_name)
        print(f"Added feature: {feature_name}")

def list_electronics():
    """List all electronic items"""
    print("List of electronic items:")
    electronics = get_all_electronics()
    for electronic in electronics:
        print(f"{electronic[0]}: {electronic[1]} ({electronic[2]}) - ${electronic[3]}")
        features = get_features_for_electronic(electronic[0])
        for feature in features:
            print(f"    - {feature[2]}")

def find_electronics():
    """Find electronic items by tag"""
    tag = input("Enter tag to search: ")

def delete_electronic_item():
    """Delete an electronic item"""
    electronic_id = int(input("Enter the ID of the electronic item to delete: "))
    delete_electronic(electronic_id)
    print(f"Deleted electronic item with ID: {electronic_id}")

def update_electronic_item():
    """Update an electronic item"""
    electronic_id = int(input("Enter the ID of the electronic item to update: "))
    name = input("New Name: ")
    brand = input("New Brand: ")
    price = float(input("New Price: "))

    update_electronic(electronic_id, name, brand, price)
    print(f"Updated electronic item with ID: {electronic_id}")

if __name__ == "__main__":
    main_menu()
