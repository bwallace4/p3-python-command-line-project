from models import User,engine,Session

mysession= Session(bind=engine)

users= mysession.query(User).all()

for user in users: 
    print (user.email)