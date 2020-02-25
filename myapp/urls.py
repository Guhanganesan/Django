from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello),
    path('', views.index),
    path('about/', views.about),
    path('sports/', views.sports),
    path('library/', views.library),
    path('articles/<str:name>/<int:date>/<int:month>/<int:year>',views.articles),
    path('student', views.stdData)
]
