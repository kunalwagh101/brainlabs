from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('check/', views.check_answer, name='check_answer'),
]
