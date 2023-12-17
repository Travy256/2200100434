from flask import Flask, render_template

app = Flask("HANK MOBILE HARDWARE",template_folder="html",static_folder="static")

app.config["TEMPLATES_AUTO_RELOAD"]=True

@app.route('/')
def home():
    return render_template("Index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

app.run(host="0.0.0.0", port=4000)