from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    # Load data
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
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
