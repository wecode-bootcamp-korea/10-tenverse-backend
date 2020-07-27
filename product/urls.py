from django.urls import path

from .views import (
    ShoesView,
    CategoryView,
    ShoeCategoryView,
)

urlpatterns = [
    path('', ShoesView.as_view()),
    path('/category', CategoryView.as_view()),
    path('/<category_name>', ShoeCategoryView.as_view()),
]
