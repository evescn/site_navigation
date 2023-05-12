from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, reverse, redirect


from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_login = request.session.get('is_login')
        if is_login != "login":
            url = request.path_info

            if url != "/login/":
                return redirect("{}?return={}".format(reverse('login'), url))

        response = self.get_response(request)

        return response

