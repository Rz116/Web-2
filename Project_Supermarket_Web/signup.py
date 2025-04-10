from flask import Flask, request, render_template, redirect
import os.path
from os import path

app = Flask(__name__)
@app.route('/')

def main():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run()
