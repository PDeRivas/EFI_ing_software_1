from django.views import View
from django.shortcuts import render, redirect

from cars.repositories.car_repository import CarsRepository
from cars.repositories.comment_repository import CommentsRepository
from cars.repositories.review_repository import ReviewsRepository
from cars.repositories.car_image_repository import CarImagesRepository

from cars.forms import CommentForm

class CarView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='car/list.html',
        )

class CarDetail(View):
    def get(self, request, id):
        car_repo = CarsRepository()
        car = car_repo.get_by_id(id=id)
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
