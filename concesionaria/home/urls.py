from django.urls import path
from django.contrib.auth.decorators import login_required

from home.views import (
    IndexView,
    LoginView,
    RegisterView,
    LogoutView,
)

urlpatterns = [
    path(route='', view=IndexView.as_view(), name='index'),
    path(route='login/', view=LoginView.as_view(), name='login'),
    path(route='register/', view=RegisterView.as_view(), name='register'),
    path(route='logout/', view=login_required(LogoutView.as_view(), login_url=('login')), name='logout'),
]