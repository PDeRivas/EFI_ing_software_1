from django.urls import path

from home.views import (
    IndexView,
)

urlpatterns = [
    path(route='', view=IndexView.as_view(), name='index'),
]