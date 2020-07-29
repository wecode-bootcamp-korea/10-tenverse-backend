import json

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import F

from .models        import (
    OrderStatus,
    Order,
    ProductOrder
)
from user.models    import User
from product.models import (
    ShoeColorSize,
    ShoeColor,
    Size
)
from utils          import login_required 

class OrderView(View):
    @login_required
    def post(self, request, user_id):
        data = json.loads(request.body)
        user = User.objects.get(id=user_id)
        try:
            product = ShoeColorSize.objects.get(
                shoecolor = ShoeColor.objects.get(id = data['id']),
                size    = Size.objects.get(name=data['size'])
            )
            if product.quantity < int(data['quantity']):
                return JsonResponse({'message' : 'OUT_OF_STOCK'}, status=400)
            if Order.objects.filter(user=user, status = OrderStatus.objects.get(name='pending')).exists():
                with transaction.atomic():
                    ProductOrder.objects.create(
                        order          = user_order,
                        product        = product,
                        order_quantity = int(data['quantity'])
                    )
                product.quantity = F('quantity') - data['quantity']
                product.save()
                return JsonResponse({'message' : 'SUCCESS'}, status=200)
            with transaction.atomic():
                user_order = Order.objects.create(user=user, status=OrderStatus.objects.get(name='pending'))
                ProductOrder.objects.create(
                    order          = user_order,
                    product        = product,
                    order_quantity = int(data['quantity'])
                )
                product.quantity = F('quantity') - int(data['quantity'])
                product.save()
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

