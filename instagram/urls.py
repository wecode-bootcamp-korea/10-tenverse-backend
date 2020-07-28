from django.urls import path

from .views import InstagramView

urlpatterns = [
    path('', InstagramView.as_view())
]
