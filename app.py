from flask import Flask
from benchmark_book import book_list

import json

app = Flask("book-sorting")

@app.route("/")
def index():
    return app.send_static_file("index.html")