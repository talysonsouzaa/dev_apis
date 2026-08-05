from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'RUBY',  'PHP', 'JS', 'TypeScript']

class habilidades(Resource):
    def get(self):
        return lista_habilidades