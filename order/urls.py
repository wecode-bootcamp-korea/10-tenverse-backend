from django.urls import path

from .views import (
    OrderView,
    PendingOrderView
)

urlpatterns = [
    path('', OrderView.as_view()),
    path('/cart', PendingOrderView.as_view())
]
