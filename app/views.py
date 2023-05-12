from django.shortcuts import render, reverse, redirect
from app import models
from app.forms import EnvForm, ServiceForm, PasswordForm
# from app import settings
from config import config

# 使用 middlewares 进行全局登陆校验，注销此方法
# def login_required(view_func):
#     def inner(request, *args, **kwargs):
#         is_login = request.session.get('is_login')
#         print(is_login, type(is_login))
#         if is_login != "login":
#             url = request.path_info
#             return redirect("{}?return={}".format(reverse('login'), url))
#         # print(request.session.session_key)
#         ret = view_func(request, *args, **kwargs)
#
#         return ret
#
#     return inner


def login(request):
    # 清理过期 session
    request.session.clear_expired()
    # 清理 session 不论是否过期
    # request.session.clear()

    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == config.Admin_User and pwd == config.Admin_Password:
            return_url = request.GET.get('return')
            if return_url:
                response = redirect(return_url)
            else:
                response = redirect(reverse('url_ops'))
            request.session['is_login'] = 'login'  # 设置数据
            # 设置会话Session和Cookie的超时时间
            request.session.set_expiry(config.Session_Time)

            return response
    return render(request, 'login.html')


# def admin(request):
#     if request.method == 'GET':
#         env_data = models.Env.objects.all()
#         # svc_data = models.Service.objects.all()
#
#         return render(request, 'admin.html', {'env_data': env_data})
#     else:
#         print('host page error!')

def view(request, eid=0):
    if request.method == 'GET':
        env_data = models.Env.objects.all()

        if int(eid) == 0:
            svc_data = models.Service.objects.all()
        elif int(eid) > 0:
            svc_data = models.Service.objects.filter(env_id_id=eid)

        return render(request, 'view.html', {'env_data': env_data, 'svc_data': svc_data})
    else:
        print('host page error!')


# @login_required
def ops(request, eid=0):
    if request.method == 'GET':
        env_data = models.Env.objects.all()

        if int(eid) == 0:
            return render(request, 'ops_env.html', {'env_data': env_data})
        elif int(eid) > 0:
            svc_data = models.Service.objects.filter(env_id_id=eid)
            return render(
                request,
                'ops_svc.html', {
                    'env_data': env_data,
                    'svc_data': svc_data,
                    'eid': eid
                }
            )
    else:
        print('host page error!')


def add_env(request):
    env_data = models.Env.objects.all()
    form_obj = EnvForm()
    if request.method == 'POST':
        form_obj = EnvForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('url_ops'))

    return render(request, 'ch_env.html', {'env_data': env_data, 'form_obj': form_obj})


def edit_env(request, eid):
    env_data = models.Env.objects.all()
    obj = models.Env.objects.filter(id=eid).first()
    form_obj = EnvForm(instance=obj)
    if request.method == 'POST':
        form_obj = EnvForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('url_ops'))

    return render(request, 'ch_env.html', {'env_data': env_data, 'form_obj': form_obj})


def del_env(request, eid):
    env_data = models.Env.objects.all()
    obj = models.Env.objects.filter(id=eid).first()
    form_env_obj = EnvForm(instance=obj)
    if request.method == 'POST':
        if eid and len(eid) > 0:
            models.Env.objects.filter(id=eid).delete()
            return redirect(reverse('url_ops'))

    return render(request, 'del_env.html', {'env_data': env_data, 'form_env_obj': form_env_obj, 'eid': eid})


def add_svc(request, eid):
    env_data = models.Env.objects.all()
    form_svc_obj = ServiceForm()
    form_pass_obj = PasswordForm()

    if request.method == 'POST':
        form_pass_obj = PasswordForm(request.POST)
        if form_pass_obj.is_valid():
            obj = form_pass_obj.save()

            name = request.POST.get('name')
            url = request.POST.get('url')
            env_id = request.POST.get('env_id')

            svc_list = {
                'name': name,
                'url': url,
                'env_id_id': env_id,
                'password_id_id': obj.id,
            }

            models.Service.objects.create(**svc_list)
            return redirect(reverse('url_ops', args=(eid,)))

    return render(
        request,
        'ch_svc.html', {
            'env_data': env_data,
            'form_svc_obj': form_svc_obj,
            'form_pass_obj': form_pass_obj,
            'eid': int(eid)
        }
    )


def edit_svc(request, eid, sid):
    env_data = models.Env.objects.all()
    svc_obj = models.Service.objects.filter(sid=sid).first()
    pass_obj = models.Password.objects.filter(id=svc_obj.password_id_id).first()

    form_svc_obj = ServiceForm(instance=svc_obj)
    form_pass_obj = PasswordForm(instance=pass_obj)

    if request.method == 'POST':
        form_pass_obj = PasswordForm(request.POST, instance=pass_obj)

        if form_pass_obj.is_valid():
            obj = form_pass_obj.save()
            name = request.POST.get('name')
            url = request.POST.get('url')
            env_id = request.POST.get('env_id')

            svc_list = {
                'name': name,
                'url': url,
                'env_id_id': env_id,
                'password_id_id': obj.id,
            }

            models.Service.objects.filter(sid=sid).update(**svc_list)
            return redirect(reverse('url_ops', args=(eid,)))

    return render(
        request,
        'ch_svc.html', {
            'env_data': env_data,
            'form_svc_obj': form_svc_obj,
            'form_pass_obj': form_pass_obj,
            'eid': int(eid)
        }
    )


def del_svc(request, eid, sid):
    env_data = models.Env.objects.all()
    svc_info = models.Service.objects.get(sid=sid)

    if request.method == 'POST':
        if eid and len(eid) > 0:
            models.Service.objects.filter(sid=sid).delete()
            return redirect(reverse('url_ops', args=(eid,)))

    return render(request, 'del_svc.html', {'env_data': env_data, 'svc_info': svc_info, 'eid': eid})
