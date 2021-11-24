from flask_restful import Resource



lista_habilidades = ['Python', 'Java', 'Flask', 'Mysql']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades