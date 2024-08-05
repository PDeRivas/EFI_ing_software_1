from django.urls import path
from django.contrib.auth.decorators import login_required
from cars.views.car_views import (
    CarView,
    CarDetail,
    )

from cars.views.comment_views import(
    CommentUpdate,
    CommentDelete,
)

from cars.views.reivew_views import(
    ReviewCreate,
    ReviewUpdate,
)

urlpatterns = [
    path(route='', view=CarView.as_view(), name='car_list'),
    path(route='<int:id>/detail/', view=CarDetail.as_view(), name='car_detail'),
    path(route='comment/<int:id>/update/', view=CommentUpdate.as_view(), name='comment_update'),
    path(route='comment/<int:id>/delete/', view=CommentDelete.as_view(), name='comment_delete'),
    path(route='review/<int:id>/', view=login_required(ReviewCreate.as_view(), login_url=('login')), name='review_create'),
    path(route='review/<int:id>/update/', view=ReviewUpdate.as_view(), name='review_update'),
]