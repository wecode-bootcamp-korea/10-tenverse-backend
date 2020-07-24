from django.urls import path

from .views import (
    ShoesView,
    CategoryView
)

urlpatterns = [
    path('', ShoesView.as_view()),
    path('/category', CategoryView.as_view()),
]
