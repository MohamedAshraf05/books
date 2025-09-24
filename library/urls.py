from django.urls import path
from . import views

urlpatterns = [
    path("books/" , views.AllBooks , name="all"),
    path("books/new/" , views.AddBook , name="new"),
    path("books/<int:book_id>/" , views.BookDetail , name="detail"),
    path("books/delete/<int:book_id>/" , views.DeleteBook , name="delete"),
    path("books/update/<int:book_id>/" , views.UpdateBook , name="update"),
]
