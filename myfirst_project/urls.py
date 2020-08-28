"""myfirst_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from canteen_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('list_food/', views.list_food, name='list_food'),
    path('add_food/', views.add_food, name='add_food'),
    path('edit_food/<int:id>/', views.edit_food, name='edit_food'),
    path('delete_food/<int:id>/', views.delete_food, name='delete_food'),
    path('', views.IndexGen.as_view(), name = 'index'),
    path('list_view', views.ListViewGen.as_view()),
    path('detail_view/<int:pk>/', views.detail_view.as_view(), name='detail_views'),
    path('search_name/', views.search_name, name='search'),
    path('create_view/', views.create_view.as_view(), name='create'),
    path('update_view/<int:phone_no>/', views.update_view.as_view(), name='update_views'),
    path('edit_cook/<int:id>/', views.edit_cook.as_view(), name='edit_cook'),
    path('create_cook/', views.create_cook.as_view(), name='create_cook'),
    path('login_form/', views.login_form, name='login'),
    path('logout_view/', views.logout_view, name='logout')
]
