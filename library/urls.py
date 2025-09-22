from django.urls import path
from . import views

urlpatterns = [
    path("books/" , views.AllBooks , name="all"),
    path("books/<int:book_id>/" , views.BookDetail , name="detail"),
    path("books/delete/<int:book_id>/" , views.BookDelete , name="delete")
]