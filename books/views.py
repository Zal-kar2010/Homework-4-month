from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book, Review, HorseTour, TourRegistration
from .forms import ReviewForm, TourRegistrationForm

# Добавьте эти функции:
def book_ru(request):
    books = Book.objects.filter(language='ru')
    return render(request, 'books/book_list.html', {
        'books': books,
        'title': 'Книги на русском языке'
    })

def book_en(request):
    books = Book.objects.filter(language='en')
    return render(request, 'books/book_list.html', {
        'books': books, 
        'title': 'Books in English'
    })

def book_usa(request):
    books = Book.objects.filter(language='usa')
    return render(request, 'books/book_list.html', {
        'books': books,
        'title': 'American Books'
    })

def tour_list(request):
    tours = HorseTour.objects.all()
    return render(request, 'books/tour_list.html', {'tours': tours})

def registration_success(request):
    return render(request, 'books/registration_success.html')

def home(request):
    try:
        books_count = Book.objects.count()
    except:
        books_count = 0
        
    try:
        tours_count = HorseTour.objects.count()
    except:
        tours_count = 0
        
    return render(request, 'books/home.html', {
        'books_count': books_count,
        'tours_count': tours_count
    })

# Ваши существующие функции оставьте без изменений:
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all().order_by('-created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'books/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'form': form
    })

@login_required
def register_for_tour(request, tour_id):
    tour = get_object_or_404(HorseTour, id=tour_id)
    if hasattr(request.user, 'tour_registration'):
        return render(request, 'books/already_registered.html')
    if request.method == 'POST':
        form = TourRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.tour = tour
            if tour.available_slots >= registration.participants:
                registration.save()
                tour.available_slots -= registration.participants
                tour.save()
                return redirect('registration_success')
            else:
                form.add_error(None, "Недостаточно свободных мест")
    else:
        form = TourRegistrationForm()
    return render(request, 'books/register_tour.html', {
        'tour': tour,
        'form': form
    })

def tours_list(request):
    tours = Book.objects.all()   # или Tours.objects.all()
    return render(request, 'books/tours_list.html', {'tours': tours})