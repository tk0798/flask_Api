from flask import Flask, request, jsonify
from wabot import WABot
import json

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    try:

        if request.method == 'POST':
            bot = WABot(request.json)
            return bot.processing()
        else:
            return "Olmadı aşkım yemedii buda"
    except Exception as e:
        return "sicti"
if(__name__) == '__main__':
    app.run()