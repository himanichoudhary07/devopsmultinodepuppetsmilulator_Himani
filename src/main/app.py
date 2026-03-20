from flask import render_template
from flask import Flask, jsonify
import random

app = Flask(__name__)

print("App starting...")

nodes = ["node1", "node2", "node3", "node4"]

def simulate_puppet():
    status = ["Success", "Failed", "In Progress"]
    return {node: random.choice(status) for node in nodes}

@app.route("/")
def home():
    return open("src/main/index.html").read()

@app.route("/api/deploy")
def deploy():
    return jsonify(simulate_puppet())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)