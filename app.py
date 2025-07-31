from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'ecommerce.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return 'API is running. Visit /api/products', 200

@app.route('/api/products', methods=['GET'])
def get_all_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return jsonify([dict(row) for row in products]), 200

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()
    conn.close()
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(dict(product)), 200

if __name__ == '__main__':
    app.run(debug=True)
