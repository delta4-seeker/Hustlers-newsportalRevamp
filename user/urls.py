from django.urls import path

from . import views
#app_name = 'user'
urlpatterns = [
    path('', views.index, name='user_index'),
    path('magazine/', views.magazine, name='magazine'),
    path('magazine/<int:id>', views.magazine_detail, name='magazine_detail'),

]