#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)


def read_products_json(filepath="products.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    products = []
    for p in data:
        products.append({
            "id": int(p["id"]),
            "name": p["name"],
            "category": p["category"],
            "price": float(p["price"])
        })
    return products


def read_products_csv(filepath="products.csv"):
    products = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


def read_products_sql(db_path="products.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    conn.close()

    products = []
    for pid, name, category, price in rows:
        products.append({
            "id": int(pid),
            "name": name,
            "category": category,
            "price": float(price)
        })
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    # Validate source
    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html", error="Wrong source", products=[])

    # Load products from the chosen source
    try:
        if source == "json":
            products_list = read_products_json()
        elif source == "csv":
            products_list = read_products_csv()
        else:  # sql
            products_list = read_products_sql()

    except FileNotFoundError:
        # Helpful (not explicitly required, but safe)
        return render_template("product_display.html", error="Data file not found", products=[])
    except sqlite3.Error:
        return render_template("product_display.html", error="Database error", products=[])
    except Exception:
        return render_template("product_display.html", error="Error reading data", products=[])

    # Optional filter by id
    if id_param is not None:
        try:
            target_id = int(id_param)
        except ValueError:
            return render_template("product_display.html", error="Product not found", products=[])

        filtered = [p for p in products_list if p["id"] == target_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])

        products_list = filtered

    return render_template("product_display.html", products=products_list, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
