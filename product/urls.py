from django.urls import path

from .views import (
    ShoesView,
    MainPageView,
    CategoryView
)

urlpatterns = [
    path('', ShoesView.as_view()),
    path('/mainpage', MainPageView.as_view()),
    path('/category', CategoryView.as_view()),
]
