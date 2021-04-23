books = input().split("&")
command = input()


while command != "Done":
    tokens = command.split(" | ")
    to_do = tokens[0]
    book_name = tokens[1]

    if to_do == 'Add Book':
        if not book_name in books:
            books.insert(0, book_name)

    elif to_do == 'Take Book':
        if book_name in books:
            books.remove(book_name)

    elif to_do == "Swap Books":
        book_two = tokens[2]
        if book_name and book_two in books:
            book_name_index = books.index(book_name)
            book_two_index = books.index(book_two)
            books[book_name_index], books[book_two_index] = books[book_two_index], books[book_name_index]

    elif to_do == "Insert Book":
        books.append(book_name)

    elif to_do == "Check Book":
        index = int(tokens[1])
        if not index > len(books):
            print(books[index])



    command = input()

print(", ".join(books))
