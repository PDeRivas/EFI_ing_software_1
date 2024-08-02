from django.urls import path
from django.contrib.auth.decorators import login_required
from cars.views.car_views import (
    CarView,
    CarDetail,
    )

urlpatterns = [
    path(route='', view=CarView.as_view(), name='car_list'),
    path(route='<int:id>/detail/', view=CarDetail.as_view(), name='car_detail'),
] 