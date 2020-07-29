from django.urls import path

from .views import (
    OrderView,
    PendingOrderView,
    UpdateOrderView
)

urlpatterns = [
    path('', OrderView.as_view()),
    path('/cart', PendingOrderView.as_view()),
    path('/update', UpdateOrderView.as_view())
]
