import pandas as pd
import sqlite3

# Load the CSV file
df = pd.read_csv('products.csv')

# Connect to SQLite DB
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Adjust table structure based on your CSV (temporary example)
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
)
''')

# Load data
df.to_sql('products', conn, if_exists='replace', index=False)

# Preview 5 rows
cursor.execute("SELECT * FROM products LIMIT 5")
for row in cursor.fetchall():
    print(row)

conn.close()
