from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book


def book_ru(request):
    return HttpResponse("Русская литература знаменита своими глубокими философскими произведениями, такими как 'Война и мир' Толстого, 'Преступление и наказание' Достоевского и 'Мастер и Маргарита' Булгакова.")

def book_en(request):
    return HttpResponse("English literature известна своим разнообразием и классикой, включая 'Harry Potter' Роулинг, 'Sherlock Holmes' Конан Дойля и 'Pride and Prejudice' Джейн Остин.")

def book_usa(request):
    return HttpResponse("American literature часто обращается к теме свободы и мечты, например, 'The Great Gatsby' Фицджеральда, 'To Kill a Mockingbird' Харпер Ли и 'Moby-Dick' Мелвилла.")


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/book_detail.html", {"book": book})

