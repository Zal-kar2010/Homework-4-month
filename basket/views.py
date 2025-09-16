# basket/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Book
from .forms import OrderForm

# 1. Просмотр всех заказов
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'basket/order_list.html', {'orders': orders})

# 2. Создание нового заказа
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    
    # Добавим книги для выбора в форме
    books = Book.objects.all()
    return render(request, 'basket/create_order.html', {'form': form, 'books': books})

# 3. Изменение заказа
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'basket/update_order.html', {'form': form})

# 4. Удаление заказа
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'basket/delete_confirm.html', {'order': order})