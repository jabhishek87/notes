import json

from flask import request
from flask_restful import abort
from flask_restful import Resource
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from .db import engine
from .db import Notes

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)


# Note
# shows a single Note item and lets you delete a Note item
class Note(Resource):
    def find_by_uuid(self, uuid):
        note = session.query(Notes).filter(Notes.uuid == uuid).first()
        if note is None:
            abort(404, message="Note {} doesn't exist".format(uuid))
        return note

    def get(self, uuid):
        note = self.find_by_uuid(uuid)
        return note.__todict__(), 200

    def delete(self, uuid):
        note = self.find_by_uuid(uuid)
        session.delete(note)
        session.commit()
        return '', 204

    def put(self, uuid):
        payload = json.loads(request.data)  # load JSON data from request
        note = self.find_by_uuid(uuid)
        note.name = payload["name"]
        note.data = payload["data"]
        session.commit()
        return note.__todict__(), 201


# NoteList
# shows a list of all Notes, and lets you POST to add new tasks
class NoteList(Resource):
    def get(self):
        resultset = session.query(Notes).all()
        all_notes = [i.__todict__() for i in resultset]
        return all_notes, 200

    def post(self):
        payload = json.loads(request.data)  # load JSON data from request
        notes = Notes(name=payload["name"], data=payload["data"])
        session.add(notes)
        session.commit()
        return notes.__todict__(), 201
