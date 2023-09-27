from flask import Flask, request, jsonify
from model import get_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Namami Gange RetrievalQA chain"

@app.route("/chat", methods=["POST"])
def chat():
    query = request.json['query']
    
    if (len(query) > 500):
        return {'query': query, 'response': "ERROR: query too long"}, 404

    response = jsonify({
        'query': query,
        'response': get_response(query)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()
