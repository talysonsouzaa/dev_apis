from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<name>')
def lovestily(name):
    return f"Eu te amo {name}"

if __name__ == '__main__':
    app.run(debug=True)