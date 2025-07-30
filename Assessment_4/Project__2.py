import datetime

class Book:
    total_books = 0  

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True 
        Book.total_books += 1

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

class Member:
    total_members = 0 

    def __init__(self, name):
        self.name = name
        self._borrowed = []  
        Member.total_members += 1

    def borrow_limit(self):
        return 0  

    def borrow(self, book, library):
        if len(self._borrowed) >= self.borrow_limit():
            print(f"{self.name} has reached their borrow limit.")
            return False
        return library.issue_book(self, book)

    def return_book(self, book, library):
        return library.return_book(self, book)

class StudentMember(Member):
    def borrow_limit(self):
        return 3  

class FacultyMember(Member):
    def borrow_limit(self):
        return 5 

class Library:
    def __init__(self):
        self.catalog = []        
        self.loans = {}          # key: member name, value: list of (book, due_date)

    def add_book(self, book):
        self.catalog.append(book)

    def find_books(self, **criteria):
        result = self.catalog
        for key, value in criteria.items():
            result = [b for b in result if getattr(b, key, '').lower() == value.lower()]
        return result

    def issue_book(self, member, book):
        if book.borrow():
            due_date = datetime.date.today() + datetime.timedelta(days=14)
            self.loans.setdefault(member.name, []).append((book, due_date))
            member._borrowed.append(book)
            print(f"Issued '{book.title}' to {member.name}. Due date: {due_date}")
            return True
        else:
            print(f"Sorry, '{book.title}' is not available.")
            return False

    def return_book(self, member, book):
        borrowed_list = self.loans.get(member.name, [])
        for b, due_date in borrowed_list:
            if b == book:
                book.return_book()
                borrowed_list.remove((b, due_date))
                member._borrowed.remove(book)
                days_overdue = (datetime.date.today() - due_date).days
                fine = max(0, days_overdue * 1)
                print(f"Returned '{book.title}'. Fine: ₹{fine}")
                return fine
        print(f"{member.name} did not borrow '{book.title}'.")
        return None

def main():
    lib = Library()

    # Sample books
    sample_books = [
        Book("The art of Being Alone", "George Orwell", "ISBN001"),
        Book("Data Structures", "Bob Jones", "ISBN003"),
        Book("Clean Code", "Robert C. Martin", "ISBN004"),
        Book("The Pragmatic Programmer", "Andrew Hunt", "ISBN005"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "ISBN006"),
        Book("To Kill a Mockingbird", "Harper Lee", "ISBN007"),
        Book("Brave New World", "Aldous Huxley", "ISBN008"),
        Book("Sapiens", "Yuval Noah Harari", "ISBN009"),
        Book("Homo Deus", "Yuval Noah Harari", "ISBN010"),
        Book("The Catcher in the Rye", "J.D. Salinger", "ISBN011"),
        Book("Thinking, Fast and Slow", "Daniel Kahneman", "ISBN012"),
        Book("Atomic Habits", "James Clear", "ISBN013"),
        Book("Deep Work", "Cal Newport", "ISBN014"),
        Book("Digital Minimalism", "Cal Newport", "ISBN015"),
        Book("The Alchemist", "Paulo Coelho", "ISBN016"),
        Book("The Power of Now", "Eckhart Tolle", "ISBN017"),
        Book("Rich Dad Poor Dad", "Robert Kiyosaki", "ISBN018"),
        Book("Zero to One", "Peter Thiel", "ISBN019"),
        Book("The Lean Startup", "Eric Ries", "ISBN020"),
        Book("Cracking the Coding Interview", "Gayle Laakmann McDowell", "ISBN021"),
        Book("Introduction to Algorithms", "Thomas H. Cormen", "ISBN022"),
        Book("Design Patterns", "Erich Gamma", "ISBN023"),
        Book("The Mythical Man-Month", "Frederick P. Brooks", "ISBN024"),
        Book("Refactoring", "Martin Fowler", "ISBN025"),
        Book("Head First Java", "Kathy Sierra", "ISBN026"),
        Book("Effective Java", "Joshua Bloch", "ISBN027"),
        Book("You Don't Know JS", "Kyle Simpson", "ISBN028"),
        Book("JavaScript: The Good Parts", "Douglas Crockford", "ISBN029"),
        Book("HTML and CSS", "Jon Duckett", "ISBN030"),
        Book("Learn Python the Hard Way", "Zed Shaw", "ISBN031"),
        Book("Python Crash Course", "Eric Matthes", "ISBN032"),
        Book("Fluent Python", "Luciano Ramalho", "ISBN033"),
        Book("Automate the Boring Stuff with Python", "Al Sweigart", "ISBN034"),
        Book("The C Programming Language", "Kernighan & Ritchie", "ISBN035"),
        Book("Operating System Concepts", "Abraham Silberschatz", "ISBN036"),
        Book("Computer Networks", "Andrew S. Tanenbaum", "ISBN037"),
        Book("Database System Concepts", "Abraham Silberschatz", "ISBN038"),
        Book("Modern Operating Systems", "Andrew S. Tanenbaum", "ISBN039"),
        Book("Artificial Intelligence", "Stuart Russell", "ISBN040"),
        Book("Machine Learning", "Tom M. Mitchell", "ISBN041"),
        Book("Deep Learning", "Ian Goodfellow", "ISBN042"),
        Book("Computer Architecture", "David A. Patterson", "ISBN043"),
        Book("Cloud Computing", "Rajkumar Buyya", "ISBN044"),
        Book("Agile Software Development", "Robert C. Martin", "ISBN045"),
        Book("Soft Skills", "John Sonmez", "ISBN046"),
        Book("The Art of Computer Programming", "Donald Knuth", "ISBN047"),
        Book("The Clean Coder", "Robert C. Martin", "ISBN048"),
        Book("Code Complete", "Steve McConnell", "ISBN049"),
        Book("Structure and Interpretation of Computer Programs", "Harold Abelson", "ISBN050"),
    ]

    for book in sample_books:
        lib.add_book(book)

    members = {}

    while True:
        print("\n--- Library Menu ---")
        print("1. Register Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. View Totals")
        print("7. Exit")

        try:
            choice = int(input("Enter your Choice: (1-7): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 7.\n")
            continue

        if choice not in [1, 2, 3, 4,5,6,7]:
            print("❌ Invalid Choice! Please select from 1 to 7.\n")
            continue


        if choice == 1:
            name = input("Enter member name: ").strip()
            type_choice = input("Enter type (student/faculty): ").strip().lower()
            if type_choice == 'student':
                members[name] = StudentMember(name)
            elif type_choice == 'faculty':
                members[name] = FacultyMember(name)
            else:
                print("Invalid member type.")

        elif choice == 2:
            title = input("Enter book title: ").strip().lower()
            author = input("Enter book author: ").strip().lower()
            isbn = input("Enter ISBN: ")
            lib.add_book(Book(title, author, isbn))
            print(f"Book '{title}' added.")

        elif choice == 3:
            name = input("Enter your name: ")
            isbn = input("Enter ISBN of the book to borrow: ")
            member = members.get(name)
            books = lib.find_books(isbn=isbn)
            if member and books:
                member.borrow(books[0], lib)
            else:
                print("Member or Book not found.")

        elif choice == 4:
            name = input("Enter your name: ")
            isbn = input("Enter ISBN of the book to return: ")
            member = members.get(name)
            books = lib.find_books(isbn=isbn)
            if member and books:
                member.return_book(books[0], lib)
            else:
                print("Member or Book not found.")

        elif choice == 5:
            search_by = input("Search by (title/author/isbn): ").lower()
            value = input(f"Enter {search_by}: ")
            results = lib.find_books(**{search_by: value})
            if results:
                print("Books found:")
                for book in results:
                    status = "Available" if book.is_available() else "Not Available"
                    print(f"{book.title} by {book.author} [{book.isbn}] - {status}")
            else:
                print("No books found.")

        elif choice == 6:
            print("Total books in library:", Book.total_books)
            print("Total registered members:", Member.total_members)

        elif choice == 7:
            print("\n")
            print("---- Exit Section ----")
            exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
            if exit_choice == 'yes':
                print("Wishing you a wonderful day ahead! 😊")
                print("Goodbye! 👋")
                break
            else:
                print("\n🔁 Taking you back to the main menu... Let's continue! 🚀\n")
if __name__ == '__main__':
    main()
