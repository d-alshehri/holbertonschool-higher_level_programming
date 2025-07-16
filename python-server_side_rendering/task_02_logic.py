from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def show_items():
    items_list = []

    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        print("Error: items.json not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from items.json.")

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
