from django.urls import path
from .views import *

urlpatterns = [
    path("books/" , BookList.as_view() , name="all"),
    path("books/new/" , AddBook.as_view() , name="new"),
    path("books/<int:pk>/" , BookDetail.as_view() , name="detail"),
    path("books/delete/<int:pk>/" , BookDelete.as_view() , name="delete"),
    path("books/update/<int:pk>/" , UpdateBook.as_view() , name="update"),
    path("login/" , CustomLoginView.as_view() , name="login"),
    path("logout/" , CustomLogoutView.as_view() ,name="logout"),
    path("register/" , RegisterView.as_view() , name="register"),
]
