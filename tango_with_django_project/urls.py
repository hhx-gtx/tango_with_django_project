"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include  # 导入 include 函数
from rango import views  # 导入 rango 应用的视图
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # 根 URL 映射到 index 视图
    path('rango/', include('rango.urls')),  # rango 应用的 URL 转交给 rango.urls
    path('admin/', admin.site.urls),
    # path('about/', include('rango.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)