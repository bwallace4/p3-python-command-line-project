from models import User,Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///models.db')
Session = sessionmaker(bind=engine)
session = Session()

user_id = input("Enter the user ID to update: ")
new_email = input("Enter the new email address: ")

user = session.query(User).filter_by(id=user_id).first()
if user:
    user.email = new_email
    session.commit()
    print("User email updated successfully!")
else:
    print("User not found.")

