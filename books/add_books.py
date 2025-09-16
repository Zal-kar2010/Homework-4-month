#!/usr/bin/env python
import os
import django
from datetime import date

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')
django.setup()

from books.models import Book

def add_sample_books():
    # Русские книги
    books_data = [
        # Русские книги
        {
            "title": "Война и мир",
            "author": "Лев Толстой", 
            "language": "ru",
            "description": "Великий роман-эпопея о русском обществе во время наполеоновских войн",
            "published_date": date(1869, 1, 1)
        },
        {
            "title": "Преступление и наказание",
            "author": "Фёдор Достоевский",
            "language": "ru", 
            "description": "Глубокий психологический роман о моральных терзаниях студента Раскольникова",
            "published_date": date(1866, 1, 1)
        },
        {
            "title": "Мастер и Маргарита",
            "author": "Михаил Булгаков",
            "language": "ru",
            "description": "Мистический роман о визите дьявола в советскую Москву",
            "published_date": date(1967, 1, 1)
        },
        {
            "title": "Анна Каренина",
            "author": "Лев Толстой",
            "language": "ru",
            "description": "Трагическая история любви и страсти в высшем обществе",
            "published_date": date(1877, 1, 1)
        },
        {
            "title": "Отцы и дети",
            "author": "Иван Тургенев",
            "language": "ru",
            "description": "Роман о конфликте поколений в России XIX века",
            "published_date": date(1862, 1, 1)
        },

        # Английские книги
        {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling",
            "language": "en",
            "description": "The first book in the magical series about a young wizard",
            "published_date": date(1997, 6, 26)
        },
        {
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "language": "en",
            "description": "Epic fantasy trilogy about the quest to destroy the One Ring",
            "published_date": date(1954, 7, 29)
        },
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "language": "en", 
            "description": "Classic romantic novel about Elizabeth Bennet and Mr. Darcy",
            "published_date": date(1813, 1, 28)
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "language": "en",
            "description": "Dystopian novel about totalitarian surveillance society",
            "published_date": date(1949, 6, 8)
        },
        {
            "title": "Sherlock Holmes: A Study in Scarlet",
            "author": "Arthur Conan Doyle",
            "language": "en",
            "description": "The first novel featuring the famous detective Sherlock Holmes",
            "published_date": date(1887, 1, 1)
        },

        # Американские книги
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "language": "usa",
            "description": "Classic novel about the American Dream in the Jazz Age",
            "published_date": date(1925, 4, 10)
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee", 
            "language": "usa",
            "description": "Powerful story about racial injustice in the American South",
            "published_date": date(1960, 7, 11)
        },
        {
            "title": "Moby-Dick",
            "author": "Herman Melville",
            "language": "usa",
            "description": "Epic tale of Captain Ahab's obsessive quest for the white whale",
            "published_date": date(1851, 10, 18)
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "language": "usa",
            "description": "Coming-of-age story about teenage rebellion and alienation",
            "published_date": date(1951, 7, 16)
        },
        {
            "title": "The Adventures of Huckleberry Finn",
            "author": "Mark Twain",
            "language": "usa",
            "description": "Adventure novel about a boy's journey down the Mississippi River",
            "published_date": date(1884, 12, 10)
        }
    ]

    for book_data in books_data:
        try:
            book, created = Book.objects.get_or_create(
                title=book_data["title"],
                author=book_data["author"],
                defaults=book_data
            )
            if created:
                print(f"Добавлена книга: {book.title}")
            else:
                print(f"Книга уже существует: {book.title}")
        except Exception as e:
            print(f"Ошибка при добавлении книги {book_data['title']}: {e}")

    print("\n✅ Процесс добавления книг завершен!")

if __name__ == "__main__":
    add_sample_books()