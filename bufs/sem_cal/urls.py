from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('seminars/<int:id>',views.detail,name='detail'),
    path('about/',views.about,name='about')
    ]
