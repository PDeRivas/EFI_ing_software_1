from django.views import View
from django.shortcuts import render, redirect

from cars.repositories.car_repository import CarsRepository
from cars.repositories.comment_repository import CommentsRepository
from cars.repositories.review_repository import ReviewsRepository
from cars.repositories.car_image_repository import CarImagesRepository

from cars.forms import CommentForm, FilterForm

class CarView(View):
    def get(self, request):
        form = FilterForm()
        return render(
            request=request,
            context={
                'form': form,
            },
            template_name='car/list.html',
        )
    
    def post(self, request):
        form = FilterForm(request.POST)
        if form.is_valid():
            price_gte = form.cleaned_data.get('price_gte') or 0
            price_lte = form.cleaned_data.get('price_lte') or 0
            brand_id = form.cleaned_data.get('brand_id') or 0
            used = form.cleaned_data.get('used')
            category_id = form.cleaned_data.get('category_id') or 0
            year_gte = form.cleaned_data.get('year_gte') or 0
            year_lte = form.cleaned_data.get('year_lte') or 0

            return redirect('car_filter', price_gte=price_gte, price_lte=price_lte, brand_id=brand_id, used=int(used), category_id=category_id, year_gte=year_gte, year_lte=year_lte)       

class CarFilter(View):
    def get(self, request, price_gte, price_lte, brand_id, used, category_id, year_gte, year_lte):
        repo = CarsRepository()
        form = FilterForm()
        cars = repo.filter_many(price_lte=price_lte,
                                price_gte=price_gte,
                                brand_id=brand_id,
                                used=used,
                                category_id=category_id,
                                year_lte=year_lte,
                                year_gte=year_gte,
                                )
        return render(
            request,
            context={
                'cars':cars,
                'form': form,
            },
            template_name='car/filter_list.html',
        )
    
    def post(self, request, price_gte, price_lte, brand_id, used, category_id, year_gte, year_lte):
        form = FilterForm(request.POST)
        if form.is_valid():
            price_gte = form.cleaned_data.get('price_gte') or 0
            price_lte = form.cleaned_data.get('price_lte') or 0
            brand_id = form.cleaned_data.get('brand_id') or 0
            used = form.cleaned_data.get('used')
            category_id = form.cleaned_data.get('category_id') or 0
            year_gte = form.cleaned_data.get('year_gte') or 0
            year_lte = form.cleaned_data.get('year_lte') or 0

            return redirect('car_filter', price_gte=price_gte, price_lte=price_lte, brand_id=brand_id, used=int(used), category_id=category_id, year_gte=year_gte, year_lte=year_lte)

class CarDetail(View):
    def get(self, request, id):
        car_repo = CarsRepository()
        car = car_repo.get_by_id(id=id)
        if not car.sold:
            comment_repo = CommentsRepository()
            comments = comment_repo.filter_by_car(car=car)
            review_repo = ReviewsRepository()
            reviews = review_repo.filter_by_car(car=car)
            car_image_repository = CarImagesRepository()
            car_images = car_image_repository.filter_by_car(car=car)

            form = CommentForm()
            return render(
                request,
                'car/detail.html',
                {
                    'car': car,
                    'comments': comments,
                    'reviews': reviews,
                    'car_images': car_images,
                    'form': form,
                }
            )
        return redirect('car_list')
    
    def post(self, request, id):
        if request.user.is_authenticated:
            if 'comment' in request.POST:
                car_repo = CarsRepository()
                comment_repo = CommentsRepository()

                car = car_repo.get_by_id(id=id)
                author = request.user
                text = request.POST.get('text')

                comment_repo.create(car=car, author=author, text=text)
            
            return redirect('car_detail', id)
        
        return redirect('login')
