from flask import Flask, render_template

app = Flask("HANK MOBILE HARDWARE",template_folder="html",static_folder="static")

app.config["TEMPLATES_AUTO_RELOAD"]=True

@app.route('/')
def home():
    return render_template("Index.html")

@app.route('/products')
def products():
    return render_template("products/index.html")

@app.route('/products/paint')
def products_paint():
    return render_template("products/paint.html")

@app.route('/products/roofing')
def products_roofing():
    return render_template("products/roofing.html")

@app.route('/products/cement')
def products_cement():
    return render_template("products/cement.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/about')
def about():
    return render_template("about.html")

app.run(host="0.0.0.0", port=4000)