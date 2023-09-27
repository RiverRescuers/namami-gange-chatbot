from flask import Flask, request, jsonify
from flask_cors import CORS
from model import get_response

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return "Namami Gange RetrievalQA chain"


@app.route("/chat", methods=["POST"])
def chat():
    query = request.json["query"]

    if query and len(query) > 500:
        response = jsonify({"query": query, "response": "ERROR: query too long"})
        status_code = 404
    else:
        response = jsonify({"query": query, "response": get_response(query)})
        status_code = 200
    return response, status_code


@app.route("/test-chat", methods=["GET"])
def test_chat():
    args = request.args
    query = args.get("query")

    if query and len(query) > 500:
        response = jsonify({"query": query, "response": "ERROR: query too long"})
        status_code = 404
    else:
        response = jsonify({"query": query, "response": get_response(query)})
        status_code = 200
    return response, status_code


if __name__ == "__main__":
    app.run()
