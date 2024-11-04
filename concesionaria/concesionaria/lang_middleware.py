from django.utils.translation import activate
from users.models import Profile

class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            lang = profile.language
            activate(lang)

        response = self.get_response(request)
        return response
