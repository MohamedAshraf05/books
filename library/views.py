from django.shortcuts import render ,redirect
from .models import Book
from django.views.generic import ListView , DetailView , DeleteView , CreateView , UpdateView
from django.views import View
from django.urls import reverse_lazy

# Create your views here.

# get all book 
# FBV function based view 
# Class Based view

# View -> GET  , POST , PUT , DELETE 


class BookList(ListView):
    model = Book
    template_name = "library/books.html"
    context_object_name = "books"

class BookDetail(DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"


class BookDelete(DeleteView):
    model = Book
    template_name = "library/books.html"
    success_url = reverse_lazy("all")


class AddBook(CreateView):
    model = Book
    template_name = "library/books.html"
    fields = ["title" , "author" , "year"]
    success_url = reverse_lazy("all")

class UpdateBook(UpdateView):
    model = Book
    template_name = "library/book_update.html"
    fields = ["title" , "author" , "year"]
    success_url = reverse_lazy("all")


# def DeleteBook(request , book_id):
#     book = Book.objects.get(id=book_id)
#     book.delete()
#     return redirect("all")

# def AddBook(request):
#     if request.method == "POST":
#         book_title = request.POST.get("book_title")
#         author = request.POST.get("book_author")
#         year = request.POST.get("book_year")
#         Book.objects.create(title=book_title , author=author , year=year)
#         return redirect("all")
#     return render(request , "library/books.html")

# def UpdateBook(request , book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == "POST":
#         book.title = request.POST.get("book_title")
#         book.author = request.POST.get("book_author")
#         book.year = request.POST.get("book_year")
#         book.save()
#         return redirect("all")
#     context = {"book" : book}
#     return render(request , "library/update.html" , context)
        