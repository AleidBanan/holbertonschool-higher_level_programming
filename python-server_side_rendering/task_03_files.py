from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        return []
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Validate Source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            p_id_int = int(product_id)
            filtered_data = [p for p in data if p['id'] == p_id_int]

            if not filtered_data:
                return render_template('product_display.html', error="Product not found")

            data = filtered_data
        except ValueError:
             return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
