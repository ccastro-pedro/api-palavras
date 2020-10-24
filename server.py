from flask import Flask, request, flash, redirect, url_for
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import classes

# Inicializar a API do Flask:
app = Flask(__name__)
api = Api(app)

words = classes.Words()


class UploadFile(Resource):
    def put(self, file):
        words.add_files(file)

api.add_resource(UploadFile, "/UploadFile/<string:file>")

class UniqueVocab(Resource):
    def get(self):
        return {'unique': words.unique_vocab}

api.add_resource(UniqueVocab, "/UniqueVocab")

class TwoGramVocab(Resource):
    def get(self):
        return {'TwoGram': words.two_gram_vocab}

api.add_resource(TwoGramVocab, "/TwoGramVocab")

class n_unique(Resource):
    def get(self):
        return words.num_unique

api.add_resource(n_unique, "/NumberUnique")

class n_TwoGram(Resource):
    def get(self):
        return words.num_two_gram

api.add_resource(n_TwoGram, "/NumberTwoGram")

if __name__ == '__main__':
    app.run(host = '0.0.0.0')