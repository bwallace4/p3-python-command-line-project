from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:///models.db", echo=True) 
Session = sessionmaker(bind=engine)
session = Session()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=False)
    email = Column(String)

def __repr__(self):
        return f"User {self.id}: "\
             + f"{self.username} "\
             + f"email: {self.email}\n"



