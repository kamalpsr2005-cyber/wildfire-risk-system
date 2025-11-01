# app.py — Flask skeleton (rebuild)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "wildfire-risk-system"})

if __name__ == '__main__':
    app.run(debug=True)
