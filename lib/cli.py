import click
import sqlite3
#from models import Electronic, Feature
#from models.electronic import Electronic
#from .helpers import add_electronic
from helpers import create_tables, add_electronic, add_feature, get_all_electronics, delete_electronic, update_electronic,get_features_for_electronic,execute_query
DATABASE = 'electronics.db'

@click.group()
def cli():
    """Electronic CLI"""
    pass

@cli.command()
def menu():
    """Display main menu"""
    while True:
        click.echo("\nPlease select an option:")
        click.echo("1. Add a new electronic item")
        click.echo("2. List all electronic items")
        click.echo("3. Find electronic items by tag")
        click.echo("4. Delete an electronic item")
        click.echo("5. Update an electronic item")
        click.echo("0. Exit")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 0:
            click.echo("Exiting program. Goodbye!")
            break
        elif choice == 1:
            add_electronic_item()
        elif choice == 2:
            list_electronics()
        elif choice == 3:
            find_electronics()
        elif choice == 4:
            delete_electronic()
        elif choice == 5:
            update_electronic()
        else:
            click.echo("Invalid choice. Please select a valid option.")

def add_electronic_item():
    """Add a new electronic item"""
    name = click.prompt("Name", type=str)
    brand = click.prompt("Brand", type=str)
    price = click.prompt("Price", type=float)
    print(name,brand,price)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO electronics (name, brand, price) VALUES (?, ?, ?)", (name, brand, price))
    electronic_id = cursor.lastrowid

    add_electronic(name,brand,price)
    #electronic = Electronic(name, brand, price)
    add_features(electronic_id)

    conn.commit()
    conn.close()

    click.echo(f"Added electronic item: {electronic_id}")

def add_features(electronic_id):
    """Add features for an electronic item"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    while True:
        feature_name = click.prompt("Enter feature name (leave blank to finish)", default="")
        if not feature_name:
            break
        cursor.execute("INSERT INTO features (electronic_id, name) VALUES (?, ?)", (electronic_id, feature_name))

    conn.commit()
    conn.close()

def list_electronics():
    """List all electronic items"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM electronics")
    electronics = cursor.fetchall()
    
    if electronics:
        click.echo("List of electronic items:")
        for electronic in electronics:
            click.echo(f"ID: {electronic[0]}, Name: {electronic[1]}, Brand: {electronic[2]}, Price: {electronic[3]}")
            cursor.execute("SELECT name FROM features WHERE electronic_id = ?", (electronic[0],))
            features = cursor.fetchall()
            for feature in features:
                click.echo(f"    Feature: {feature[0]}")
    else:
        click.echo("No electronic items found.")
    
    conn.close()

def find_electronics():
    """Find electronic items by tag"""
    tag = click.prompt("Enter tag to search", type=str)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM electronics WHERE name LIKE ? OR brand LIKE ?", (f'%{tag}%', f'%{tag}%'))
    electronics = cursor.fetchall()

    if electronics:
        for electronic in electronics:
            click.echo(f"ID: {electronic[0]}, Name: {electronic[1]}, Brand: {electronic[2]}, Price: {electronic[3]}")
    else:
        click.echo("No electronic items found with the given tag.")
    
    conn.close()

def delete_electronic():
    """Delete an electronic item"""
    electronic_id = click.prompt("Enter the ID of the electronic item to delete", type=int)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM electronics WHERE id = ?", (electronic_id,))
    cursor.execute("DELETE FROM features WHERE electronic_id = ?", (electronic_id,))
    conn.commit()
    conn.close()
    click.echo("Electronic item deleted.")

def update_electronic():
    """Update an electronic item"""
    electronic_id = click.prompt("Enter the ID of the electronic item to update", type=int)
    name = click.prompt("Enter new name", type=str)
    brand = click.prompt("Enter new brand", type=str)
    price = click.prompt("Enter new price", type=float)
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE electronics SET name = ?, brand = ?, price = ? WHERE id = ?", (name, brand, price, electronic_id))
    conn.commit()
    conn.close()
    click.echo("Electronic item updated.")

if __name__ == "__main__":
    create_tables()
    cli()
