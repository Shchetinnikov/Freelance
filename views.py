from flask import flash, render_template, request

from app import app


@app.route('/')
def index():
    return render_template("index.html", text='Это Рябушка')
