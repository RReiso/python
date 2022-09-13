def main():
    try:
        bookList = []
        infile = open("bookList.txt", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("No file to read - bookList.txt\n")
        print("Starting a new list\n")

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display all books ")
        print("4) Quit ")

        try:
            choice = int(input())

            if choice == 1:
                print("Adding a book...")
                nBook = input("Enter the name of the book >>>>")
                nAuthor = input("Enter the name of the author >>>>")
                nPages = input("Enter the number of pages >>>>")
                bookList.append([nBook, nAuthor, nPages])
                print("The book has been added to the list!")

            elif choice == 2:
                print("Looking up for a book...")
                keyword = input("Enter search Term: ")
                for book in bookList:
                    if keyword in book:
                        print(book)

            elif choice == 3:
                print("Displaying all books...")
                for i in range(len(bookList)):
                    print(bookList[i])

            elif choice == 4:
                print("Quitting program")

            else:
                print("Wrong input")

        except ValueError:
            print("Wrong input")

    outfile = open("bookList.txt", "w")
    for book in bookList:
        print(book)
        outfile.write(",".join(book) + "\n")
    outfile.close()


# if the name of the file == main, do...
if __name__ == "__main__":
    main()
