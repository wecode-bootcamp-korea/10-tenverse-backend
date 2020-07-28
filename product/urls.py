from django.urls import path

from .views import (
    ShoesView,
    DetailView,
    MainPageView,
    CategoryView
)

urlpatterns = [
    path('', ShoesView.as_view()),
    path('/detail/<product_id>', DetailView.as_view()),
    path('/mainpage', MainPageView.as_view()),
    path('/category', CategoryView.as_view()),
]
