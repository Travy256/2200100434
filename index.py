from flask import Flask, render_template

app = Flask("HANK ONLINE HARDWARE",template_folder="html",static_folder="static")

app.config["TEMPLATES_AUTO_RELOAD"]=True

@app.route('/')
def home():
    return render_template("Index.html")

@app.route('/about')
def about():
    return render_template("about.html")

app.run()    

