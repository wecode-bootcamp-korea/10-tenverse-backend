from django.urls import path

from .views import (
    ShoeCategoryView,
    MainPageView,
    DetailView
)

urlpatterns = [
    path('/<category_name>', ShoeCategoryView.as_view()),
    path('/detail/<product_id>', DetailView.as_view()),
    path('', MainPageView.as_view()),
]
