from django.shortcuts import render
from tags.models import Product


#все продукты
def all_products(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-id') # - последний добавленный элемент отображается первым
        context = {
            'products': products,
        }
    return render(request, 'tags/all_products.html', context=context)

#Напитки
def drinks_products(request):
    if request.method == 'GET':
        products = Product.objects.filter(tags__name='#Напитки').order_by('-id') # - последний добавленный элемент отображается первым
        context = {
            'products': products,
        }
    return render(request, 'tags/drinks_products.html', context=context)

#Еда
def meal_products(request):
    if request.method == 'GET':
        products = Product.objects.filter(tags__name='#Еда').order_by('-id') # - последний добавленный элемент отображается первым
        context = {
            'products': products,
        }
    return render(request, 'tags/meal_products.html', context=context)