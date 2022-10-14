from django.shortcuts import render, reverse, redirect
from django.shortcuts import HttpResponse
from app import models
import json


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
        # print(request.session.session_key)
        ret = view_func(request, *args, **kwargs)

        return ret

    return inner


def login(request):
    request.session.clear_expired()
    # print('123')
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == '123':
            return_url = request.GET.get('return')
            if return_url:
                response = redirect(return_url)
            else:
                response = redirect(reverse('url_ops'))

            # response.set_cookie('is_login', '1')
            # response.set_signed_cookie('is_login', '1',salt='xxxx')
            request.session['is_login'] = 1  # 设置数据
            # request.session['user'] = models.Publisher(name='xxx')
            # 设置会话Session和Cookie的超时时间
            # request.session.set_expiry(5)

            return response
    return render(request, 'login.html')


def admin(request):
    if request.method == 'GET':
        env_data = models.Env.objects.all()
        # svc_data = models.Service.objects.all()

        return render(request, 'admin.html', {'env_data': env_data})
    else:
        print('host page error!')


@login_required
def ops(request, eid=0):
    if request.method == 'GET':
        env_data = models.Env.objects.all()
        print('eid: ', eid)
        svc_data = models.Service.objects.filter(env_id_id=eid)

        return render(request, 'ops.html', {'env_data': env_data, 'svc_data': svc_data})
    else:
        print('host page error!')


@login_required
def add_env(request):
    if request.method == 'GET':
        return render(request, 'add_env.html')

    elif request.method == 'POST':
        print(request.method)
        print(request.POST)
        ret = {'status': True, 'error': None}
        try:

            name = request.POST.get('name')
            env_list = {
                'name': name,
            }
            models.Env.objects.create(**env_list)

        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '请求错误'

        return HttpResponse(json.dumps(ret))


@login_required
def edit_env(request, id):
    print(id)
    print(request.method)

    if request.method == 'GET':
        env_info = models.Env.objects.get(id=id)
        # print(env_info)
        return render(request, 'edit_env.html', {'env_info': env_info})

    elif request.method == 'POST':
        print(request.POST)
        # print(request.POST.get(id=id))
        ret = {'status': True, 'error': None, 'data': None}
        try:
            new_id = request.POST.get('id')
            print(new_id)
            if new_id != id:
                ret['status'] = False
                ret['error'] = '太短了'
                return redirect(reverse('url_edit_env'))
            else:
                name = request.POST.get('name')
                if id and len(id) > 0:
                    env_list = {
                        'name': name,
                    }
                    models.Env.objects.filter(id=id).update(**env_list)

                else:
                    ret['status'] = False
                    ret['error'] = '太短了'

        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '请求错误'

        return HttpResponse(json.dumps(ret))


@login_required
def ajax_del_env(request, id):
    print(id)
    if request.method == 'GET':
        # host_info = models.Host.objects.get(id=id)
        env_info = models.Env.objects.get(id=id)
        print(env_info)
        return render(request, 'del_env.html', {'env_info': env_info})

    elif request.method == 'POST':
        ret = {'status': True, 'error': None, 'data': None}
        try:
            id = request.POST.get('id')
            name = request.POST.get('name')

            print(id, name, sep='\t')

            if id and len(id) > 0:
                print('===========')
                models.Env.objects.filter(id=id).delete()
                # models.Env.remove(id=id).delete()

            else:
                ret['status'] = False
                ret['error'] = 'new_id不对'

        except Exception as e:
            ret['status'] = False
            ret['error'] = '请求错误'

        return HttpResponse(json.dumps(ret))


@login_required
def add_svc(request):
    if request.method == 'GET':
        env_list = models.Env.objects.all()
        return render(request, 'add_svc.html', {'env_list': env_list})

    elif request.method == 'POST':
        ret = {'status': True, 'error': None}
        try:
            name = request.POST.get('name')
            url = request.POST.get('url')
            user = request.POST.get('user')
            password = request.POST.get('password')
            env_id = request.POST.get('env_id')

            password_list = {
                'user': user,
                'password': password
            }

            obj = models.Password.objects.create(**password_list)
            print(obj.id)
            print(type(obj.id))
            svc_list = {
                'name': name,
                'url': url,
                'env_id_id': env_id,
                'password_id_id': obj.id,

            }
            print(svc_list)
            models.Service.objects.create(**svc_list)

        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '请求错误'

        return HttpResponse(json.dumps(ret))


@login_required
def edit_svc(request, sid):
    # print(sid)
    if request.method == 'GET':
        env_list = models.Env.objects.all()
        svc_info = models.Service.objects.get(sid=sid)
        password_info = models.Password.objects.get(id=svc_info.password_id_id)
        return render(request, 'edit_svc.html',
                      {'svc_info': svc_info, 'env_list': env_list, 'password_info': password_info})

    elif request.method == 'POST':
        ret = {'status': True, 'error': None, 'data': None}
        try:
            new_id = request.POST.get('sid')
            if new_id != sid:
                ret['status'] = False
                ret['error'] = 'new_id不对'
                return redirect(reverse('url_edit_env', sid))

            else:
                if sid and len(sid) > 0:
                    name = request.POST.get('name')
                    url = request.POST.get('url')
                    pid = request.POST.get('pid')
                    user = request.POST.get('user')
                    password = request.POST.get('password')
                    env_id = request.POST.get('env_id')

                    password_list = {
                        'user': user,
                        'password': password
                    }
                    models.Password.objects.filter(id=pid).update(**password_list)

                    svc_list = {
                        'name': name,
                        'url': url,
                        'env_id_id': env_id,
                    }

                    models.Service.objects.filter(sid=sid).update(**svc_list)

                else:
                    ret['status'] = False
                    ret['error'] = '太短了'

        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '请求错误'

        return HttpResponse(json.dumps(ret))


@login_required
def ajax_del_svc(request, sid):
    print(sid)
    svc_info = models.Service.objects.get(sid=sid)
    if request.method == 'GET':
        print(svc_info)
        return render(request, 'del_svc.html', {'svc_info': svc_info})

    elif request.method == 'POST':
        ret = {'status': True, 'error': None, 'data': None}
        try:
            sid = request.POST.get('sid')
            name = request.POST.get('name')

            print(sid, name, sep='\t')

            if sid and len(sid) > 0:
                print('===========')
                models.Password.objects.filter(id=svc_info.password_id_id).delete()
                models.Service.objects.filter(sid=sid).delete()
                # models.Env.remove(id=id).delete()

            else:
                ret['status'] = False
                ret['error'] = '太短了'

        except Exception as e:
            ret['status'] = False
            ret['error'] = '请求错误'

        return HttpResponse(json.dumps(ret))


def view(request, eid):
    if request.method == 'GET':
        env_data = models.Env.objects.all()
        # print('eid: ', eid)
        svc_data = models.Service.objects.filter(env_id_id=eid)

        return render(request, 'view.html', {'env_data': env_data, 'svc_data': svc_data})
    else:
        print('host page error!')
