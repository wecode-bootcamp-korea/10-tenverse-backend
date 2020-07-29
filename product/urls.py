from django.urls import path

from .views import (
   # ShoesView,
    ShoeCategoryView,
    #MainPageView,
)

urlpatterns = [
    #path('', ShoesView.as_view()),
    #path('/mainpage', MainPageView.as_view()),
    path('/<category_name>', ShoeCategoryView.as_view()),
]
