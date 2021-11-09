import requests
from flask import Flask, request

# https://github.com/fawazahmed0/currency-api
CURRENCIES_API = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/"


app = Flask(__name__)


@app.route("/home")
def newhome():
    return "Home"


@app.route("/")
def home():
    print(request.args.get("param"))
    return "Welcome."


@app.route("/currencies")
def currencies():
    endpoint = "currencies"
    r = requests.get(f"{CURRENCIES_API}{endpoint}.json")
    return r.json()


@app.route("/currencies/<currencycode>")
def currencyvalues(currencycode):
    endpoint = f"currencies/{currencycode}"
    r = requests.get(f"{CURRENCIES_API}{endpoint}.json")
    return r.json()


@app.route("/currencies/<currencycodefrom>/<currencycodeto>")
def currencyvalue(currencycodefrom, currencycodeto):
    endpoint = f"currencies/{currencycodefrom}/{currencycodeto}"
    r = requests.get(f"{CURRENCIES_API}{endpoint}.json")
    return r.json()
