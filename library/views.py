from django.shortcuts import render ,redirect
from .models import Book
from django.views.generic import ListView
# Create your views here.

# get all book 
# FBV function based view 
# Class Based view

# class BookList(ListView):
#     model = Book
#     template_name = "library/books.html"
#     context_object_name = "books"


def AllBooks(request):
    books = Book.objects.all()
    context = {"books" : books}
    return render(request , "library/books.html" , context)

# detail view 
def BookDetail(request , book_id):
    book = Book.objects.get(id=book_id)
    context = {"book" : book}
    return render(request , "library/book_detail.html" , context)


def DeleteBook(request , book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("all")

def AddBook(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        author = request.POST.get("book_author")
        year = request.POST.get("book_year")
        Book.objects.create(title=book_title , author=author , year=year)
        return redirect("all")
    return render(request , "library/books.html")

def UpdateBook(request , book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("book_title")
        book.author = request.POST.get("book_author")
        book.year = request.POST.get("book_year")
        book.save()
        return redirect("all")
    context = {"book" : book}
    return render(request , "library/update.html" , context)
        