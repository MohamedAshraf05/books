from django.shortcuts import render ,redirect
from .models import Book
# Create your views here.

# get all book 

def AllBooks(request):
    books = Book.objects.all()
    context = {"books" : books}
    return render(request , "library/books.html" , context)

# detail view 
def BookDetail(request , book_id):
    book = Book.objects.get(id=book_id)
    context = {"book" : book}
    return render(request , "library/book_detail.html" , context)



# def BookDelete(request , book_id):
#     book = Book.objects.get(id=book_id)
#     book.delete()
#     return render(request , "library/book_detail.html")