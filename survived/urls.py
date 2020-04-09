from django.urls import path

from . import views

urlpatterns = [
    path('api/survived/', views.SurvivedListCreate.as_view()),
]
