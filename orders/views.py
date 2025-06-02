from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order
from services.models import Service

def create_order(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.service = service
            order.save()
            return redirect('order_status', order_id=order.id)  # або інша сторінка після успішної заявки
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form, 'service': service})


def choose_service(request):
    services = Service.objects.all()
    return render(request, 'orders/choose_service.html', {'services': services})

def thank_you(request):
    return render(request, 'orders/thank_you.html')

def order_lookup(request):
    error = ''
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                # Якщо замовлення знайшлось — перенаправляємо на сторінку статусу
                return redirect('order_status', order_id=order_id)
            except Order.DoesNotExist:
                error = "Замовлення з таким номером не знайдено."
        else:
            error = "Введіть номер замовлення."

    return render(request, 'orders/order_lookup.html', {'error': error})

# Перегляд статусу
def order_status(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        error = "Замовлення з таким номером не знайдено."
        return render(request, 'orders/order_lookup.html', {'error': error})
    
    return render(request, 'orders/order_status.html', {'order': order})