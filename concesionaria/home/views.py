from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout)

class IndexView(View):
    def get(self, request):
        return render(
        request,
        'home/index.html'
        )