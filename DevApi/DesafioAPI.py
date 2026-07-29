from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {"id": 0, "Responsavel":"Talyson", "tarefa":["Fazer uma API"], "Status":"Pendente"},
    {"id": 1, "Responsavel":"Mariana", "tarefa":["Fazer o FrontEnd"], "Status":"Concluida"}
]
@app.route('/<int:id>/', methods=['GET', 'PUT'])
def lista(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = f"Tarefa de {id} nao existe"
            response = {"Status": "erro", "Mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido, procure o ADM"
            response = {"Status": "erro", "Mensagem": mensagem}

        return jsonify(response)

    elif request.method == 'PUT':
        try:
            dados = json.loads(request.data)
            tarefas[id]["status"] = dados["status"]
            tarefas[id]["tarefa"] = dados["tarefa"]
            
            return jsonify(dados)
        except IndexError:
            return jsonify({"Status": "erro", "Mensagem": f"Tarefa de {id} nao existe"})

    elif request.method == 'DELETE':
        try:
            tarefas.pop(id)
            return jsonify({"Status": "sucesso", "Mensagem": "Tarefa removida"})
        except IndexError:
            return jsonify({"Status": "erro", "Mensagem": f"Tarefa de {id} nao existe"})

if __name__=='__main__':
    app.run(debug=-True)