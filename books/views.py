from django.http import HttpResponse

def book_ru(request):
    return HttpResponse("Русская литература знаменита своими глубокими философскими произведениями, такими как 'Война и мир' Льва Толстого, 'Преступление и наказание' Фёдора Достоевского и 'Мастер и Маргарита' Михаила Булгакова, которые исследуют судьбу человека, мораль и смысл жизни.")

def book_en(request):
    return HttpResponse("English literature известна своим разнообразием и классикой, включая 'Harry Potter' Дж. К. Роулинг, 'The Adventures of Sherlock Holmes' Артура Конан Дойля и 'Pride and Prejudice' Джейн Остин, которые отражают воображение, загадки и социальные отношения.")

def book_usa(request):
    return HttpResponse("American literature часто обращается к теме свободы и мечты, примеры — 'The Great Gatsby' Фрэнсиса Скотта Фицджеральда, 'To Kill a Mockingbird' Харпер Ли и 'Moby-Dick' Германа Мелвилла, где поднимаются вопросы справедливости, природы человека и американской мечты.")


# Create your views here.
