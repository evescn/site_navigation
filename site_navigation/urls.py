"""site_navigation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from app import views
from django.conf.urls import url


urlpatterns = [
    path('login/', views.login, name='login'),
    path('ops/', views.ops, name='url_ops'),
    re_path('ops/(?P<eid>\d+)', views.ops, name='url_ops'),

    path('add_env/', views.add_env, name='url_add_env'),
    re_path('edit_env/(?P<id>\d+)', views.edit_env, name='url_edit_env'),
    re_path('del_env/(?P<id>\d+)', views.ajax_del_env, name='url_del_env'),

    path('add_svc/', views.add_svc, name='url_add_svc'),
    re_path('edit_svc/(?P<sid>\d+)', views.edit_svc, name='url_edit_svc'),
    re_path('del_svc/(?P<sid>\d+)', views.ajax_del_svc, name='url_del_svc'),

    # path('admin_admin/', admin.site.urls),

    # 定义默认访问路由，表示输入任意url路径
    re_path(r'view/(?P<eid>\d+)', views.view, name='url_view'),
    url(r'^$', views.admin, name='url_admin'),
]
