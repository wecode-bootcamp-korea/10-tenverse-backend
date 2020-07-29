import json

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import (
    F,
    Count
)

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
            user_order = Order.objects.get(user=user, status = OrderStatus.objects.get(name='pending'))
            with transaction.atomic():
                try:
                    order = ProductOrder.objects.get(order = user_order, product = product, order_quantity = int(data['quantity']))
                    order.order_quantity = F('order_quantity') + data['quantity']
                    order.save()
                except ProductOrder.DoesNotExist:
                    ProductOrder.objects.create(
                        order          = user_order,
                        product        = product,
                        order_quantity = int(data['quantity'])
                    )
                product.quantity = F('quantity') - data['quantity']
                product.save()
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except Order.DoesNotExist:
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

class PendingOrderView(View):
    @login_required
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        order_list = ProductOrder.objects.filter(
            order = Order.objects.get(
                user   = User.objects.get(id = user_id),
                status = OrderStatus.objects.get(name = "pending")
            )).prefetch_related(
            "product",
            "product__shoecolor",
            "product__shoecolor__color",
            "product__shoecolor__shoe",
            "product__shoecolor__shoe__detail",
            "product__size",
            "product__shoecolor__image"
        )

        pending_orders = [
            {
                "id"       : order.product.id,
                "image"    : order.product.shoecolor.image.image,
                "name"     : order.product.shoecolor.shoe.detail.name,
                "price"    : order.product.shoecolor.shoe.price,
                "color"    : order.product.shoecolor.color.name,
                "size"     : order.product.size.name,
                "quantity" : order.order_quantity
            } for order in order_list
        ]
        return JsonResponse({"pending_orders" : pending_orders}, status=200)

