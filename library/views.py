from django.shortcuts import render ,redirect
from .models import Book
from django.views.generic import ListView , DetailView , DeleteView , CreateView , UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = "library/login.html"


class CustomLogoutView(LogoutView):
    next_page = "login"


class RegisterView(View):
    def get(self , request):
        return render(request , "library/registration.html")

    def post(self , request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request , "Password do not match")
            return render(request ,"library/registration.html")

        if User.objects.filter(username=username).exists():
            messages.error(request , "Username already taken")
            return render(request , "library/registration.html")

        user = User.objects.create_user(username=username , password=password)
        login(request , user)
        return redirect("all")


class BookList(LoginRequiredMixin , ListView):
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

        