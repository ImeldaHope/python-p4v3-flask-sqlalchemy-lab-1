from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, String, Integer, Float
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "eathquakes"

    id = Column(Integer(), primary_key = True)
    magnitude = Column(Float())
    location = Column(String())
    year = Column(Integer())

    def __init__(self, magnitude=None, location=None, year=None, id=None):
        self.id = id  
        self.magnitude = magnitude
        self.location = location
        self.year = year

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
