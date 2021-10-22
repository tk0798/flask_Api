from flask import Flask, request
from wabot import WABot
import json

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    return "sicti"
