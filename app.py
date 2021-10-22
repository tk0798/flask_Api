from flask import Flask, request
from wabot import WABot
import json

# app = Flask(__name__)


from flask import Flask # flask kütüphanemizi projemize import ettik.

app = Flask(__name__) # app değişkenizimizin Flask olduğunu belirttik.

@app.route("/") # Endpoint imizi tanımladık.
def hello(): # Bir fonksiyon oluşturduk.
    return "Hello World" # Sitemizde görmek istediğimiz şeyi return ettik.

if(__name__) == '__main__':
    app.run()