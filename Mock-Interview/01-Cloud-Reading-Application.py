'''
Online cloud reading app, similar to Amazon kindle
Need help designing actual application

- Users have a library of books that they can add to or remove from.
- Users can set a book from their library as active
- The reading application remembers where a user left off in a given book
- The reading application only displays a page of text at a time in the active book
'''

'''
Object oriented programming
structuring..

- flag var: active / not
- flag var: pg #

- class method: add
- class method: remove
- class method: returns flagged var page

----

video suggests:
- remember all books in the library
- remember active books
- remember last pages in all books
- display a page in active book

- one class - represeting a book (Book)
    - id: str/int ?
    - title: str
    - pages / content: list of str (per pg)
    - last page user looked at: int (remember off-by-one)
- another class - representing the library
    - collection of books: { id: book() }
    - active book: var correspond to id
'''

class Book:

    def __init__(self, id, title, content) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0
    
    def display_page(self):
        return self.content[self.last_page]
    
    # when user is reading the book and changing the pages
    def update_page(self):
        self.last_page += 1
        return self.display_page()


class Library:

    def __init__(self) -> None:
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0 # simple unique counter for now
    
    def add_to_collection(self, title, content):
        new_book = Book(self.id_counter, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1

    # removing from the collection
    # recruiter: is it going to save a copy?
    def remove_from_collection(self, id):
        del self.collection[id]

    # if user is setting an active book, we can only have 1 active book
    def set_active_book(self, id):
        self.active_book = id

    # display the page of where user left off
    def display_page(self):
        return self.collection[self.active_book].display_page()
    
    def turn_page(self):
        return self.collection[self.active_book].update_page()
    

'''
Follow up question:
older reader needs bigger font size, how to handle this?
how to refactor the page or implement in logic?

video suggest:
self.font_size = 12
self.chars_per_page = calc(self.font_size)

def display_page(self):
start_idx = self.chars_per_page * self.last_page
end_idx = start_idx + self.chars_per_page
return self.content[start_idx: end_idx]

---

New follow up question:
multiple users in the system and all share books
how to implement the quality of the book?

video suggest:
SQL table, can just return the book in the table
'''