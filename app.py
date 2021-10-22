from flask import Flask, request
from wabot import WABot
import json

# app = Flask(__name__)


from flask import Flask # flask kütüphanemizi projemize import ettik.

app = Flask(__name__) # app değişkenizimizin Flask olduğunu belirttik.

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        bot = WABot(request.json)
        return bot.processing()

# if(__name__) == '__main__':
#     app.run()