from datetime import datetime

from django.views import View
from django.shortcuts import render, redirect

from cars.repositories.car_repository import CarsRepository
from cars.repositories.sale_repository import SalesRepository
from cars.forms import SaleForm
from cars.models import Country

class SaleView(View):
    def get(self, request, id):
        repo = CarsRepository()
        car = repo.get_by_id(id=id)
        if not car.sold:
            form = SaleForm()
            return render(
                request=request,
                template_name='sale/create.html',
                context={
                    'car': car,
                    'form': form,
                },
            )
        else:
            return redirect('car_list')

    def post(self, request, id):
        car_repo = CarsRepository()
        car = car_repo.get_by_id(id=id)
        if not car.sold:
            sale_repo = SalesRepository()
            buyer = request.user
            credit_card_number = request.POST.get('credit_card_number')
            country_id = request.POST.get('country')
            country = Country.objects.get(id=country_id)
            city = request.POST.get('city')
            postal_code = request.POST.get('postal_code')
            phone = request.POST.get('phone')
            date = datetime.now().date()
            time = datetime.now().time()

            sale_repo.create(car=car,
                                buyer=buyer,
                                credit_card_number=credit_card_number,
                                country=country,
                                city=city,
                                postal_code=postal_code,
                                phone=phone,
                                date=date,
                                time=time)
        return redirect('car_list')
    
class SaleList(View):
    def get(self, request):
        if request.user.is_staff:
            repo = SalesRepository()
            sales = repo.get_all()
            return render(
                request=request,
                template_name='sale/list.html',
                context={
                    'sales': sales,
                },
            )
        else:
            return redirect('car_list')