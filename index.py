from flask import Flask, request
from flask_cors import CORS
from markupsafe import escape
from model import get_response

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return "Namami Gange RetrievalQA chain"

@app.route("/chat", methods=["POST"])
def chat():
    query = request.json['query']
    
    if (len(query) > 500):
        return {'query': query, 'response': "ERROR: query too long"}, 404

    return {
        'query': query,
        'response': escape(get_response(query[:100]))
    }

if __name__ == '__main__':
    app.run()
