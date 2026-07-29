from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>/<Prof>/<Name>')
def Ola(id, Prof, Name):
  return jsonify({'id':id, 'nome': Name, 'Prof': Prof})

#@app.route('/soma/<int:v1>/<int:v2>')
#def soma(v1 , v2):
#   return jsonify({'soma':v1 + v2})

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})

if __name__ == '__main__':#
    app.run(debug=True)