from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"id":1,"name":"iPhone 15","category":"Mobile"},
    {"id":2,"name":"Samsung S24","category":"Mobile"},
    {"id":3,"name":"Apple Watch","category":"Accessory"},
    {"id":4,"name":"AirPods Pro","category":"Accessory"},
]

@app.route("/")
def home():

    viewed_product = products[0]

    recommendations = [
        products[2],
        products[3]
    ]

    return render_template(
        "index.html",
        products=products,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)