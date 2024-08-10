from typing import (
    List,
    Optional,
)

from django.contrib.auth.models import User

from cars.models import(
    Car,
    Review,
)

class ReviewsRepository:
    def create(self,
               car: Car,
               author: User,
               text: str,
               rating: int,
               ) -> Review:
        return Review.objects.create(
            car = car,
            author = author,
            text = text,
            rating = rating,
        )
    
    def update(self,
                review: Review,
                text: str,
                rating: int,
                date,
                time,):
        review.text = text
        review.rating = rating
        review.date_edit = date
        review.time_edit = time
        review.save()

    def delete(self, review: Review):
        review.delete()

    def get_all(self) -> List[Review]:
        return Review.objects.all()
    
    def get_by_id(self, id: int,) -> Optional[Car]:
        try:
            review = Review.objects.get(id=id)
        except:
            review = None
        return review
    
    def filter_by_car(self, car: Car,) -> Optional[List[Review]]:
        return Review.objects.filter(car=car)

    def filter_by_rating(self, car: Car, rating: int) -> Optional[List[Review]]:
        return Review.objects.filter(car=car, rating=rating)

    def user_has_review(self, user: User, car: Car):
        if len(Review.objects.filter(author=user, car=car).values()) != 0:
            return True
        return False
