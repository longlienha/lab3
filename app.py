from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index() :
    return "Hello!"

@app.route("/tambiet")
def tambiet() :
    return jsonify({"about":"longhuu"})

if __name__ == "__main__":
    app.run(debug=True)