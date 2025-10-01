from django.contrib import admin
from .models import Book , Author
# Register your models here.


# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title" , "author" , "id" , "created_at"]
    ordering = ["id"]

admin.site.register(Author)