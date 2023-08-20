from models import User,Session,engine

mysession= Session(bind=engine)


new_user = User(username='Alice', email='alice@example.com')
new_user1 = User(username='Bob', email='bob@example.com')


mysession.add(new_user)
mysession.add(new_user1)


mysession.commit()


# new_user = User(username='brandon nimmo', email='john@example.com')
# new_user1 = User(username='jose altuve', email='tuve@example.com')

# Session.add(new_user ,new_user1)
# Session.commit()



# engine = create_engine('sqlite:///models.db')




