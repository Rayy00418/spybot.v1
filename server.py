from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"data/{file.filename}")
    return "Uploaded"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
