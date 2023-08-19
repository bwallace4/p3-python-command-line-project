from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

engine = create_engine("sqlite:///models.db", echo=True) 



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=False)
    email = Column(String)

def __repr__(self):
        return f"User {self.id}: "\
             + f"{self.name} "\
             + f"email: {self.email}\n"


Brandon_nimmo = User(username='brandon nimmo', email='john@example.com')
print(Brandon_nimmo )