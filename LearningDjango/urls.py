"""LearningDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from . import view, testdb

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 函数include()允许引用其它URLconfs
    # path(route, view, kwargs?, name?)
    # 参数route：是url的一个正则式匹配，越严格的式子越靠前，跟Node.js里的Koa很像
    path('TestModel/', include('TestModel.urls')),
    path('admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),

]
