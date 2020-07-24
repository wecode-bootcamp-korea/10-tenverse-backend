from django.urls import path

from .views import (
    ShoesView,
    MainPageView,
)

urlpatterns = [
    path('', ShoesView.as_view()),
    path('/mainpage', MainPageView.as_view()),
]
