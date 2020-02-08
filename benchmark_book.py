from librazzo import Book
from selection_sort_book import selection_sort

book1 = Book("Dante", "Divina Commedia")
book2 = Book("Boccaccio", "Canzoniere")
book3 = Book("Petrarca", "Decamerone")

book_list = [book1,book2,book3]

print(f"lista prima: {[x.author for x in book_list]}")

selection_sort(book_list)

print(f"lista dopo: {[x.author for x in book_list]}")
