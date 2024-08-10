from datetime import datetime

from django.views import View
from django.shortcuts import render, redirect

from cars.repositories.car_repository import CarsRepository
from cars.repositories.review_repository import ReviewsRepository

from cars.forms import ReviewForm

class ReviewCreate(View):
    def get(self, request, id):
        review_repo = ReviewsRepository()
        repo = CarsRepository()
        car = repo.get_by_id(id=id)
        if not review_repo.user_has_review(user=request.user, car=car):
            form = ReviewForm()

            return render(
                request=request,
                template_name='review/create.html',
                context={
                    'car': car,
                    'form': form,
                },
            )
        else:
            return redirect('car_detail', id)

    def post(self, request, id):
        if request.user.is_authenticated:
            car_repo = CarsRepository()
            review_repo = ReviewsRepository()

            car = car_repo.get_by_id(id=id)
            author = request.user
            text = request.POST.get('text')
            rating = request.POST.get('rating')

            review_repo.create(car=car, author=author, text=text, rating=rating)
            return redirect('car_detail', id)
        
        return redirect('login')
    
class ReviewUpdate(View):
    def get(self, request, id):
        review_repo = ReviewsRepository()
        review = review_repo.get_by_id(id)
        car = review.car
        form = ReviewForm()
        if review.author == request.user:
            return render(
                request=request,
                template_name='review/update.html',
                context={
                    'car': car,
                    'form': form,
                }
            )
        else:
            return redirect('car_detail', review.car.id)

    def post(self, request, id):
        review_repo = ReviewsRepository()
        review = review_repo.get_by_id(id)
        if review.author == request.user:
            text = request.POST.get('text')
            rating = request.POST.get('rating')
            date = datetime.now().date()
            time = datetime.now().time()

            review_repo.update(review=review,text=text, rating=rating, date=date, time=time)
        
        return redirect('car_detail', review.car.id)
    