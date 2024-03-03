books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]

def check_books(book):
    if(book["rating"] > 4.5):
        return "high"
    elif(book["rating"] > 4.0):
        return "medium"
    else:
        return "low"
    
def average_rating_by_genre(books, genre):
    total = 0
    count = 0
    for i in books:
        if (i["genre"] == genre):
            total += i["rating"]
            count += 1
    if(count != 0):
        return total/count
    else:
        return "Genre doesn't exist"
    
def books_by_author(books, author):
    listOfBooks = []
    for i in books:
        if(i["author"] == author):
            listOfBooks.append(i["title"])
    if(len(listOfBooks) != 0):
        return listOfBooks
    else:
        return "Author doesn't exist"
