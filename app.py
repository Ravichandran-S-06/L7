
import sqlite3
from datetime import datetime


conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# Function to create tables if they don't exist
def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS flavors (
                      id INTEGER PRIMARY KEY,
                      name TEXT UNIQUE NOT NULL,
                      season TEXT,
                      available BOOLEAN DEFAULT 1)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                      id INTEGER PRIMARY KEY,
                      name TEXT UNIQUE NOT NULL,
                      quantity INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                      id INTEGER PRIMARY KEY,
                      customer_name TEXT NOT NULL,
                      suggested_flavor TEXT,
                      allergy_concern TEXT,
                      suggestion_date TEXT)''')
    conn.commit()

# Call this function to set up tables initially
create_tables()

# Function to add a seasonal flavor
def add_seasonal_flavor(name, season):
    cursor.execute("INSERT INTO flavors (name, season) VALUES (?, ?)", (name, season))
    conn.commit()
    print(f"Flavor '{name}' added for the {season} season.")

# Function to manage ingredient inventory
def update_ingredient(name, quantity):
    cursor.execute("INSERT OR REPLACE INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    print(f"Ingredient '{name}' updated with quantity: {quantity}")

# Function for customer flavor suggestion
def add_customer_suggestion(customer_name, flavor, allergy):
    date = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO customer_suggestions (customer_name, suggested_flavor, allergy_concern, suggestion_date) VALUES (?, ?, ?, ?)",
                   (customer_name, flavor, allergy, date))
    conn.commit()
    print(f"Suggestion from '{customer_name}' added with flavor '{flavor}' and allergy concern '{allergy}'.")



# Close the database connection when done
def close_connection():
    conn.close()
