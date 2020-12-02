from django.urls import path
from . import views

urlpatterns = [
    path('api/catalogue/', views.BookListCreate.as_view()),
]