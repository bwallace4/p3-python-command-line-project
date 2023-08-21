from models import User,Session,engine

def main():
    session = Session()

    # Create an author and their books
    author = Author(name="J.K. Rowling")
    book1 = Book(title="Harry Potter and the Sorcerer's Stone", author=author)
    book2 = Book(title="Harry Potter and the Chamber of Secrets", author=author)
    session.add(author)
    session.commit()

    # Create reviews for a book
    review1 = Review(content="A magical adventure!", book=book1)
    review2 = Review(content="Even better than the first!", book=book1)
    session.add_all([review1, review2])
    session.commit()

    # Query and print data
    selected_author = session.query(Author).first()
    print(f"Author: {selected_author.name}")
    for book in selected_author.books:
        print(f"Book: {book.title}")
        for review in book.reviews:
            print(f"  Review: {review.content}")

if __name__ == "__main__":
    main()

# mysession= Session(bind=engine)


# new_user = User(username='Alice', email='alice@example.com')
# new_user1 = User(username='Bob', email='bob@example.com')


# mysession.add(new_user)
# mysession.add(new_user1)


# mysession.commit()


# new_user = User(username='brandon nimmo', email='john@example.com')
# new_user1 = User(username='jose altuve', email='tuve@example.com')

# Session.add(new_user ,new_user1)
# Session.commit()



# engine = create_engine('sqlite:///models.db')




