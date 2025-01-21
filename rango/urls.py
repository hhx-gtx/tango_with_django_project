from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),  # 映射空路径到 index 视图
    path('about/', views.about, name='about'),
]