from librazzo import Book
from selection_sort_book import selection_sort

book1 = Book("Dante", "Petrarca")
book2 = Book("Canzoniere", "Boccaccio")
book3 = Book("Decamerone", "Divina Commedia")

book_list = [book1,book2,book3]

selection_sort(book_list)
