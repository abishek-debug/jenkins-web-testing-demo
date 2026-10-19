from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Health Check Application is running!"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "Health Check App"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
