import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

import uuid
from settings import SQLALCHEMY_DATABASE_URI

engine = db.create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()


class Notes(Base):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, unique=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String)
    data = db.Column(db.Text)

    def __repr__(self):
        return "<notes(name={}, uuid={})>".format(self.name, self.uuid)

    def __todict__(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "data": self.data,
        }


def init_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()
