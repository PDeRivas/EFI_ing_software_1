from typing import (
    List,
    Optional,
)

from django.contrib.auth.models import User

from cars.models import(
    Car,
    Comment,
)

class CommentsRepository:
    def create(self,
               car: Car,
               author: User,
               text: str,
               ) -> Comment.objects:
        
        return Comment.objects.create(
            car = car,
            author = author,
            text = text,
        )
    
    def update(self, comment: Comment, text: str):
        comment.text = text
        comment.save()

    def delete(self, comment: Comment):
        comment.delete()

    def get_all(self) -> List[Comment]:
        return Comment.objects.all()
    
    def get_by_id(self, id: int,) -> Optional[Car]:
        try:
            comment = Comment.objects.get(id=id)
        except:
            comment = None
        return comment
    
    def filter_by_car(self, car: Car,) -> Optional[List[Comment]]:
        return Comment.objects.filter(car=car)
        return comment.car
