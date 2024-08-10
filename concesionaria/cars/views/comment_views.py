from datetime import datetime

from django.views import View
from django.shortcuts import render, redirect
from cars.repositories.comment_repository import CommentsRepository
from cars.forms import CommentForm

class CommentUpdate(View):
    def get(self, request, id):
        comment_repo = CommentsRepository()
        comment = comment_repo.get_by_id(id=id)
        if comment.author == request.user:
            car = comment.car
            text = comment.text
            form = CommentForm()
            return render(
                request,
                'comment/update.html',
                {
                    'car': car,
                    'text': text,
                    'form': form,
                }
            )
        else:
            return redirect('car_detail', comment.car.id)
    
    def post(self, request, id):
        comment_repo = CommentsRepository()
        comment = comment_repo.get_by_id(id=id)
        text = request.POST.get('text')
        date = datetime.now().date()
        time = datetime.now().time()
        comment_repo.update(comment=comment, text=text, date=date, time=time)
        car = comment.car

        return redirect('car_detail', car.id)
    
class CommentDelete(View):
    def get(self, request, id):
        comment_repo = CommentsRepository()
        comment = comment_repo.get_by_id(id=id)
        if comment.author == request.user or request.user.is_staff:
            comment_repo.delete(comment=comment)
        return redirect('car_detail', comment.car.id)
