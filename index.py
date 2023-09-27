from flask import Flask, request
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return "hello world"

@app.route("/chat", methods=["POST"])
def chat():
    query = request.json['query']
    return {
        'query': query,
        'respones': escape("aaa" + query[:100])
    }

if __name__ == '__main__':
    app.run()
