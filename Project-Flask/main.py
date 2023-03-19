from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

""" 
############## Returning a file sample
def download():
    return send_from_directory('static', filename="files/Standard_template.xlsx")

"""
if __name__ == "__main__":
    app.run(debug=True)
