from flask import Flask, request, json
from flask_restful import Resource, Api
from habilidades import habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0, 'nome':'Talyson', 'habilidades':['Python', 'Flask']},
    {'id': 1, 'nome':'Mariana', 'habilidades':['JS', 'Front']},
    {'id': 2, 'nome':'Eduarda', 'habilidades':['Java', 'Backend']}
]

#devolve, altera e deleta desenvolvedores da lista pelo ID
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'Status':'Erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido procure o ADM'
            response = {'Status': 'Erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads (request.data)
        desenvolvedores[id] == dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return{'Status':'Sucesso', 'mensagem':'Registro Excluido'}


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
            return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(habilidades, '/habilidades/')
if __name__ == '__main__':
    app.run(port=5001)