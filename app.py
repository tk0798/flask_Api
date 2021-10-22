from flask import Flask, request, jsonify
from wabot import WABot
import json

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        bot = WABot(request.json)
        return bot.processing()
    else:
        return "Olmadı aşkım yemedii buda"

if(__name__) == '__main__':
    app.run()