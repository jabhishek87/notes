from flask import Flask
from flask_restful import Api

from api.api import Note, NoteList

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(NoteList, '/notes')
api.add_resource(Note, '/notes/<uuid>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)  # nosec
