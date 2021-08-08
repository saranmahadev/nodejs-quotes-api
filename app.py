from flask import Flask
import json
import random

app = Flask(__name__)

with open("quotes.json") as quotes:
    data = json.load(quotes)

@app.route('/quotes/all')
def all_quotes():    
    return { 
        "quotes" :  data , 
        "size" : len(data), 
        "status" : "success" 
    }

@app.route('/quotes/<number>')
def number_quotes(number):        
    quote = []
    try:
        num = int(number)
    except:
        return {
            "status" : "error",
            "message" : "Invalid number"
        }

    for i in range(0,num):
        quote.append(random.choice(data))
    return {
        "quotes" : quote,
        "size" : len(quote),
        "status" : "success"        
    }

@app.route('/quotes/single')
def single_quote():    
    return {
        "quote" : random.choice(data),
        "status" : "success"
    }
    
@app.errorhandler(Exception)
def handle_error(e):    
    return {
        "status" : "error",
        "message" : str(e)
    }

if __name__ == '__main__':
    app.run(port=8080)