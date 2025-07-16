from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_products():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []

def read_csv_products():
    products = []
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
    except Exception:
        pass
    return products

def read_sql_products():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    # Load data based on source
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    elif source == 'sql':
        products = read_sql_products()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Filter by ID (optional)
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
