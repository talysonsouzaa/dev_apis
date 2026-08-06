from flask_restful import Resource
from flask import json, request

lista_habilidades = ['Python', 'Java', 'RUBY',  'PHP', 'JS']

class habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados['lista_habilidades'])
        return lista_habilidades[posicao]

class put_del(Resource):
    def delete(self, id):
        lista_habilidades.pop(id)
        return {
            'Status':'Sucesso',
            'message': 'A habilidade foi excluida com sucesso'
        }
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados