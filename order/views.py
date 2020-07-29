import json

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import (
    F,
    Count,
    Sum,
    IntegerField
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
                "price"    : int(order.product.shoecolor.shoe.price),
                "color"    : order.product.shoecolor.color.name,
                "size"     : order.product.size.name,
                "quantity" : order.order_quantity
            } for order in order_list
        ]
        total_price = int(order_list.aggregate(
            price = Sum(
                F('order_quantity')*F('product__shoecolor__shoe__price'),
                output_field=IntegerField()
            ))['price'])

        return JsonResponse({"total_price" : total_price, "pending_orders" : pending_orders}, status=200)

class UpdateOrderView(View):
    @login_required
    def post(self, request, user_id):
        data = json.loads(request.body)
        user = User.objects.get(id=user_id)
        try:
            product_order = ProductOrder.objects.get(id=data['id']).prefetch_related("product__shoecolor")
            with transaction.atomic():
                product_order.product.quantity = product.shoecolor.quantity + (product_order.order_quantity - data['quantity'])
                product_order.order_quantity = data['quantity']
                product_order.product.quantity.save()
                product_order.order_quantity.save()
            return JsonResponse({'message' : 'KeyError'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'KeyError'}, status=400)

