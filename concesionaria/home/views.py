from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import (
    authenticate,
    login,
    logout)
from users.forms import UserLoginForm, UserRegisterForm
from django.utils.translation import activate

from users.models import Profile

class IndexView(View):
    def get(self, request):
        return render(
            request,
            'home/index.html'
        )
    
class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = UserLoginForm()
            return render(
                request,
                'home/login.html',
                {
                    'form': form,
                }
            )
        else:
            return redirect('/')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request,
                                username=username,
                                password=password)
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')
    
class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form':form
            }  
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'form':form
            }
        )
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class UpdateLang(View):
    def get(self, request):
        profile = Profile.objects.get(user = request.user)
        lang = profile.language
        if lang == 'es':
            profile.language = 'en'
        if lang == 'en':
            profile.language = 'es'
        profile.save()

        return redirect(request.META.get('HTTP_REFERER', 'index'))
