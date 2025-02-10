import jsonpickle

class Book:
    
    def __init__(self, __id, __title, __author, __content):
        self.__id__ = __id #TODO: do not expose
        self.__title__ = __title
        self.__author__= __author
        self.__content__ = __content


class BookStore:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books


class Library:
    pass


class User:
    pass

class App:
    def __init__(self):
        self.__actions__ = {
            'ls': self.list_books,
            'new': self.new_book
        }
        self.__book_store__ = BookStore()
        self.__library = Library()
    
    def list_books(self):
        print ('book_store.list()')
        
    def new_book(self):
        title = input('title: ')
        author = input ('author: ')
        content = input ('content: ')
        book = Book(0, author, title, content)
        self.__book_store.add(book)
        
    def delete_book(self):
        book_title = input('Enter the title of the book to delete: ')
        for book in self.books:
            if book['title'] == book_title:
                self.books.remove(book)
                print(f"Book '{book_title}' deleted successfully.")
                return
        print(f"Book '{book_title}' not found.")
    
    def get_book(self):
        books = self.__book_store__.get_books()
        for book in books:
            print(f"ID: {book.__id__}, Title: {book.__title__}, Author: {book.__author__}, Content: {book.__content__}")
    
    def save_to_disk(self):
        with open('my_lib.json', 'w') as lib_file:
            raw_json = jsonpickle.encode(self.__library)
            lib_file.write(raw_json)
        with open('my book_store.json', 'w') as book_store_file:
            raw_json = jsonpickle.encode(self.__book_store)
            book_store_file.write(raw_json)
    
    def run(self):
            action = input('Action ? ')
            self.__actions__[action]()
            
if __name__ == '__main__':
    
    app = App()
    app.run()