from django.urls import path

from .views import (
    ShoesView,
    DetailView
)

urlpatterns = [
    path('', ShoesView.as_view()),
    path('/<int:product_id>', DetailView.as_view())
]
