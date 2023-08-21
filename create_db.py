from models import Director, Movie, Review, Session, engine, Base

Base.metadata.create_all(engine)