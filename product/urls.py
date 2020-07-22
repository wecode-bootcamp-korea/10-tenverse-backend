from django.urls import path

from .views import ShoesView

urlpatterns = [
    path('', ShoesView.as_view()),
]
