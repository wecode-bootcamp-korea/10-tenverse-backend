from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('product', include('product.urls')),
    path('instagram', include('instagram.urls')),
    path('order', include('order.urls'))
]
