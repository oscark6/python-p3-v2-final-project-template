import sqlite3

DATABASE = "electronics.db"

def execute_query(query, params=(), fetchall=False, fetchone=False, commit=False):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if commit:
                conn.commit()
            if fetchall:
                return cursor.fetchall()
            if fetchone:
                return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in execute_query: {e}")
    return None

def create_tables():
    execute_query("""
        CREATE TABLE IF NOT EXISTS electronics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            brand TEXT NOT NULL,
            price REAL NOT NULL
        )
    """, commit=True)

    execute_query("""
        CREATE TABLE IF NOT EXISTS features (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            electronic_id INTEGER,
            feature_name TEXT NOT NULL,
            FOREIGN KEY (electronic_id) REFERENCES electronics (id)
        )
    """, commit=True)

def add_electronic(name, brand, price):
    execute_query("""
        INSERT INTO electronics (name, brand, price)
        VALUES (?,?,?)
    """, (name, brand, price), commit=True)

def get_all_electronics():
    return execute_query("SELECT * FROM electronics", fetchall=True)

def find_electronics_by_name(name):
   # return execute_query("SELECT * FROM electronics WHERE tags LIKE ?", (f"%{tag}%",), fetchall=True)
  # return execute_query("SELECT * FROM electronics WHERE name = ?", (name,))
  conn = sqlite3.connect('electronics.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM electronics WHERE name = ?", (name,))
  electronic = cursor.fetchone()
  conn.close()
  return electronic

def delete_electronic(electronic_id):
    execute_query("DELETE FROM electronics WHERE id=?", (electronic_id,), commit=True)

def update_electronic(electronic_id, name, brand, price):
    execute_query("""
        UPDATE electronics
        SET name=?, brand=?, price=?
        WHERE id=?
    """, (name, brand, price, electronic_id), commit=True)

def add_feature(electronic_id, feature_name):
    execute_query("""
        INSERT INTO features (electronic_id, feature_name)
        VALUES (?,?)
    """, (electronic_id, feature_name), commit=True)

def get_features_for_electronic(electronic_id):
    return execute_query("SELECT * FROM features WHERE electronic_id=?", (electronic_id,), fetchall=True)

class Electronic:
    def __init__(self, name, brand, price):  
        self.name = name
        self.brand = brand
        self.price = price
        self.features = []

    def __repr__(self):  
        return f"<Electronic(name={self.name}, brand={self.brand}, price={self.price})>"

class Feature:
    def __init__(self, feature_name): 
        self.feature_name = feature_name

    def __repr__(self):  
        return f"<Feature(name={self.feature_name})>"
