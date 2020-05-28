from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home page'),
    path('expression', views.expression, name='expression value'),
    path('about', views.abouts, name='about page'),

]