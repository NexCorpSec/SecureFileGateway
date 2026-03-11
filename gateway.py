from flask import Flask, request, jsonify
import os

app = Flask(__name__)

FILES_PATH = "./storage"

@app.route("/files")
def list_files():
    files = os.listdir(FILES_PATH)
    return jsonify(files)

@app.route("/download")
def download():
    name = request.args.get("name")

    path = os.path.join(FILES_PATH, name)

    if not os.path.exists(path):
        return jsonify({"error": "file not found"}), 404

    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    app.run(port=5001)
