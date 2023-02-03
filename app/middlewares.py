from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, reverse, redirect


class MD1(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('123')
        print(view_func)
        print(view_args)
        print(view_kwargs)
        def login_required(view_func):
            def inner(request, *args, **kwargs):
                # is_login = request.COOKIES.get('is_login')
                # is_login = request.get_signed_cookie('is_login',salt='xxxx',default='')
                is_login = request.session.get('is_login')
                print(is_login, type(is_login))
                if is_login != 1:
                    # http://127.0.0.1:8000/app01/author/
                    url = request.path_info
                    return redirect("{}?return={}".format(reverse('login'), url))
                print(request.session.session_key)
                ret = view_func(request, *args, **kwargs)

                return ret

            return inner

        is_login = request.session.get('is_login')
        print(is_login, type(is_login))
        if is_login != 1:
            # http://127.0.0.1:8000/app01/author/
            url = request.path_info
            return redirect("{}?return={}".format(reverse('login'), url))

        # return login_required()

