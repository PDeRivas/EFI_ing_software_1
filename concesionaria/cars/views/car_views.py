from django.views import View
from django.shortcuts import render, redirect
from cars.repositories.car_repository import CarsRepository

class CarView(View):
    def get(self, request):
        repo = CarsRepository()
        cars = repo.get_all()

        return render(
            request=request,
            template_name='car/list.html',
            context={
             'cars': cars
            },
        )

class CarDetail(View):
    def get(self, request, id):
        repo = CarsRepository()
        car = repo.get_by_id(id=id)
        try:
            imagen = ProductImage.objects.get(product=car)
        except:
            imagen = None

        return render(
            request,
            'car/detail.html',
            {
                'car': car,
                'image': imagen,
            }
        )