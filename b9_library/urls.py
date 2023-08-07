"""
URL configuration for b9_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import welcome_page,show_all_books,show_single_book,add_single_book,edit_single_book,delete_single_book
from app.views import form_view
from user_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',welcome_page,name='home_page'),
    path('show-book/',show_all_books,name='show_books'),
    path('show-single-book/<int:id>',show_single_book,name='show_single_book'),
    path('add-single-book/',add_single_book,name='add_single_book'),
    path('edit-single-book/<int:id>',edit_single_book,name='edit_single_book'),
    path('delete-single-book/<int:id>',delete_single_book,name='delete_single_book'),
    path('form-view/',form_view,name='form_view'),
    path("user-register/",views.user_register,name="user_register"),

]

# image.png