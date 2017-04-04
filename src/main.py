from flask import Flask, request
from src import location

APP = Flask(__name__)

APP.add_url_rule('/', 'location', location.post_location, methods=["POST"])

def start():
    APP.run(port='8080')

if __name__ == "__main__":
    start()