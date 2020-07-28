from django.urls import path

from .views import (
    ShoesView,
    DetailView,
    FilterView
)

urlpatterns = [
    path('', ShoesView.as_view()),
    path('/detail/<product_id>', DetailView.as_view()),
    path('/filter', FilterView.as_view())
]
