from django.shortcuts import render
from .models import Car
def show_data(request):
    if request.method == 'POST':
        cars_brand = request.POST.get('cars_brand')
        release_date = request.POST.get('release_date')
        cars_colour = request.POST.get('cars_colour')
        cars_probeg = request.POST.get('cars_probeg')
        cars_price = request.POST.get('cars_price')
        Car.objects.create(cars_brand=cars_brand,
                           release_date=release_date,
                           cars_colour=cars_colour,
                           cars_price=cars_price,
                           cars_probeg=cars_probeg)
    return render(request, 'index.html')
def get_data(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        context = {'cars': cars}
    return render(request, 'res.html', context=context)



