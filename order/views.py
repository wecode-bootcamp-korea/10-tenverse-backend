from django.views import View
from django.http  import JsonResponse

from .models        import (
    OrderStatus,
    Order,
    ProductOrder
)
from user.models    import User
from product.models import ShoeColorSize
from utils          import login_required        
