from flask import Flask
from flask_restful import Resource, Api
import classes


# Inicializar a API do Flask:
app = Flask(__name__)
api = Api(app)

words = classes.Words()


class UploadFile(Resource):
    """
    Chamar o API para adicionar um novo arquivo (método add_files da classe Words)
    """
    def put(self, file):
        words.add_files(file)

api.add_resource(UploadFile, "/UploadFile/<string:file>")

class UniqueVocab(Resource):
    """
    Chamar o API para visualizar o vocabulário de palavras únicas
    """
    def get(self):
        return {'unique': words.unique_vocab}

api.add_resource(UniqueVocab, "/UniqueVocab")

class TwoGramVocab(Resource):
    """
    Chamar o API para visualizar o vocabulário de Two Gram
    """
    def get(self):
        return {'TwoGram': words.two_gram_vocab}

api.add_resource(TwoGramVocab, "/TwoGramVocab")

class n_unique(Resource):
    """
    Chamar o API para visualizar os vetores de palavras únicas de cada texto
    """
    def get(self):
        return words.num_unique

api.add_resource(n_unique, "/NumberUnique")

class n_TwoGram(Resource):
    """
    Chamar o API para visualizar os vetores de Two Gram de cada texto
    """
    def get(self):
        return words.num_two_gram

api.add_resource(n_TwoGram, "/NumberTwoGram")

if __name__ == '__main__':
    app.run(host = '0.0.0.0')