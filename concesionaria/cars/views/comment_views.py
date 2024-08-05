from django.views import View
from django.shortcuts import render, redirect
from cars.repositories.car_repository import CarsRepository
from cars.repositories.comment_repository import CommentsRepository

class CommentUpdate(View):
    def get(self, request, id):
        comment_repo = CommentsRepository()
        comment = comment_repo.get_by_id(id=id)
        if comment.author == request.user:
            car = comment.car
            text = comment.text

            return render(
                request,
                'comment/update.html',
                {
                    'car': car,
                    'text': text,
                }
            )
        else:
            return redirect('car_detail', comment.car.id)
    
    def post(self, request, id):
        comment_repo = CommentsRepository()
        comment = comment_repo.get_by_id(id=id)
        text = request.POST.get('text')
        comment_repo.update(comment=comment, text=text)
        car = comment.car

        return redirect('car_detail', car.id)
    
class CommentDelete(View):
    def get(self, request, id):
        comment_repo = CommentsRepository()
        comment = comment_repo.get_by_id(id=id)
        if comment.author == request.user or request.user.is_staff:
            comment_repo.delete(comment=comment)
        return redirect('car_detail', comment.car.id)
