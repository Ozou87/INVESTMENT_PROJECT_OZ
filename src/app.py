
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return " ❤ מוקה גור שמח שאת מרגישה טוב יותר"

if __name__ == "__main__":
    app.run(debug=True)
