from flask import Flask, request, jsonify
from wabot import WABot
import json

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():

        return "sicti"
if(__name__) == '__main__':
    app.run()