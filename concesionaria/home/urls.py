from django.urls import path

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
    path(route='logout/', view=LogoutView.as_view(), name='logout')
]