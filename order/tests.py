import jwt
import json

from django.test import (
    TestCase,
    Client
)

from user.models import (
    User,
    Gender
)
from product.models import (
    MainCategory,
    ShoeCategory,
    Size,
    ColorFilter,
    Color,
    TypeFilter,
    GenderSegmentation,
    Detail,
    Shoe,
    ShoeColorSize,
    MainImage,
    ShoeColor,
    SubImage
)
from .models    import (
    OrderStatus,
    Order,
    ProductOrder
)
from utils      import login_required

class OrderViewTest(TestCase):
    maxDiff = None

    def setUp(self):
        MainCategory.objects.create(id=1, name='신발')
        ShoeCategory.objects.create(id=1, main_category = MainCategory.objects.get(id=1), name='척 70')
        Detail.objects.create(id=1, main_detail='test', sub_detail='test', feature='test', feature_image='test')
        Size.objects.create(id=1, name=220)
        ColorFilter.objects.create(id=1, name='black')
        Color.objects.create(id=1, color_category=ColorFilter.objects.get(id=1),name='블랙')
        TypeFilter.objects.create(id=1, name='스니커즈')
        GenderSegmentation.objects.create(id=1, name='남녀공용')
        Shoe.objects.create(
            id=1,
            main_category = MainCategory.objects.get(id=1),
            shoe_category = ShoeCategory.objects.get(id=1),
            type_filter = TypeFilter.objects.get(id=1),
            detail = Detail.objects.get(id=1),
            gender_segmentation = GenderSegmentation.objects.get(id=1),
            price=95000.00
        )
        MainImage.objects.create(id=1, image='image')
        ShoeColor.objects.create(
            id=1,
            shoe = Shoe.objects.get(id=1),
            color = Color.objects.get(id=1),
            image = MainImage.objects.get(id=1)
        )
        ShoeColorSize.objects.create(id=1, shoecolor=ShoeColor.objects.get(id=1), size=Size.objects.get(id=1), quantity=2)
        SubImage.objects.create(id=1, image='image', is_hovered=True)
        Gender.objects.create(id=1, name='여성')
        User.objects.create(
            id = 1,
            email = 'test@test.com',
            password = 'a1234!dddd',
            phone_number = '01012341234',
            gender = Gender.objects.get(id=1),
            birth_date = '2020-07-28',
            name = 'test'
        )
        OrderStatus.objects.create(id=1, name='pending')
        
    def tearDown(self):

        MainCategory.objects.all().delete()
        ShoeCategory.objects.all().delete()
        ColorFilter.objects.all().delete()
        Color.objects.all().delete()
        TypeFilter.objects.all().delete()
        GenderSegmentation.objects.all().delete()
        Detail.objects.all().delete()
        Shoe.objects.all().delete()
        MainImage.objects.all().delete()
        ShoeColor.objects.all().delete()
        SubImage.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        OrderStatus.objects.all().delete()

    def test_orderview_success(self):
        client = Client()
        header = {"HTTP_Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.6mlhvmw9MyBvInOVrhOnQNizB8iPI47xZ_2sC1gUcXs"}
        order = {
            'id' : 1,
            'size' : 220,
            'quantity' : 1
        }
        response = client.post('/order', json.dumps(order),content_type = 'application/json', **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})

class PendingOrderViewTest(TestCase):
    maxDiff = None

    def setUp(self):
        MainCategory.objects.create(id=1, name='신발')
        ShoeCategory.objects.create(id=1, main_category = MainCategory.objects.get(id=1), name='척 70')
        Detail.objects.create(id=1, name='test', main_detail='test', sub_detail='test', feature='test', feature_image='test')
        Size.objects.create(id=1, name=220)
        ColorFilter.objects.create(id=1, name='black')
        Color.objects.create(id=1, color_category=ColorFilter.objects.get(id=1),name='블랙')
        TypeFilter.objects.create(id=1, name='스니커즈')
        GenderSegmentation.objects.create(id=1, name='남녀공용')
        Shoe.objects.create(
            id=1,
            main_category = MainCategory.objects.get(id=1),
            shoe_category = ShoeCategory.objects.get(id=1),
            type_filter = TypeFilter.objects.get(id=1),
            detail = Detail.objects.get(id=1),
            gender_segmentation = GenderSegmentation.objects.get(id=1),
            price=95000.00
        )
        MainImage.objects.create(id=1, image='image')
        ShoeColor.objects.create(
            id=1,
            shoe = Shoe.objects.get(id=1),
            color = Color.objects.get(id=1),
            image = MainImage.objects.get(id=1)
        )
        ShoeColorSize.objects.create(id=1, shoecolor=ShoeColor.objects.get(id=1), size=Size.objects.get(id=1), quantity=2)
        SubImage.objects.create(id=1, image='image', is_hovered=True)
        Gender.objects.create(id=1, name='여성')
        User.objects.create(
            id = 1,
            email = 'test@test.com',
            password = 'a1234!dddd',
            phone_number = '01012341234',
            gender = Gender.objects.get(id=1),
            birth_date = '2020-07-28',
            name = 'test'
        )
        OrderStatus.objects.create(id=1, name="pending")
        Order.objects.create(id=1,user=User.objects.get(id=1), status = OrderStatus.objects.get(name="pending"))
        ProductOrder.objects.create(id=1, order = Order.objects.get(id=1), product=ShoeColorSize.objects.get(id=1), order_quantity=1)

    def tearDown(self):
        Gender.objects.all().delete()
        User.objects.all().delete()
        OrderStatus.objects.all().delete()
        Order.objects.all().delete()
        ProductOrder.objects.all().delete()

    def test_pendingorder_success(self):
        client = Client()
        header = {"HTTP_Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.6mlhvmw9MyBvInOVrhOnQNizB8iPI47xZ_2sC1gUcXs"}
        
        response = client.get('/order/cart', content_type = 'application/json', **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "pending_orders" : [
                {
                    "id" : 1,
                    "image" : "image",
                    "price" : 95000,
                    "name" : "test",
                    "color" : "블랙",
                    "size" : 220,
                    "quantity" : 1
                }
            ]
        })

class UpdateOrderViewTest(TestCase):
    maxDiff = None
    
    def setUp(self):
        MainCategory.objects.create(id=1, name='신발')
        ShoeCategory.objects.create(id=1, main_category = MainCategory.objects.get(id=1), name='척 70')
        Detail.objects.create(id=1, name='test', main_detail='test', sub_detail='test', feature='test', feature_image='test')
        Size.objects.create(id=1, name=220)
        ColorFilter.objects.create(id=1, name='black')
        Color.objects.create(id=1, color_category=ColorFilter.objects.get(id=1),name='블랙')
        TypeFilter.objects.create(id=1, name='스니커즈')
        GenderSegmentation.objects.create(id=1, name='남녀공용')
        Shoe.objects.create(
            id=1,
            main_category = MainCategory.objects.get(id=1),
            shoe_category = ShoeCategory.objects.get(id=1),
            type_filter = TypeFilter.objects.get(id=1),
            detail = Detail.objects.get(id=1),
            gender_segmentation = GenderSegmentation.objects.get(id=1),
            price=95000.00
        )
        MainImage.objects.create(id=1, image='image')
        ShoeColor.objects.create(
            id=1,
            shoe = Shoe.objects.get(id=1),
            color = Color.objects.get(id=1),
            image = MainImage.objects.get(id=1)
        )
        ShoeColorSize.objects.create(id=1, shoecolor=ShoeColor.objects.get(id=1), size=Size.objects.get(id=1), quantity=2)
        SubImage.objects.create(id=1, image='image', is_hovered=True)
        Gender.objects.create(id=1, name='여성')
        User.objects.create(
            id = 1,
            email = 'test@test.com',
            password = 'a1234!dddd',
            phone_number = '01012341234',
            gender = Gender.objects.get(id=1),
            birth_date = '2020-07-28',
            name = 'test'
        )
        OrderStatus.objects.create(id=1, name="pending")
        Order.objects.create(id=1,user=User.objects.get(id=1), status = OrderStatus.objects.get(name="pending"))
        ProductOrder.objects.create(id=1, order = Order.objects.get(id=1), product=ShoeColorSize.objects.get(id=1), order_quantity=1)

    def tearDown(self):
        MainCategory.objects.all().delete()
        ShoeCategory.objects.all().delete()
        ColorFilter.objects.all().delete()
        Color.objects.all().delete()
        TypeFilter.objects.all().delete()
        GenderSegmentation.objects.all().delete()
        Detail.objects.all().delete()
        Shoe.objects.all().delete()
        MainImage.objects.all().delete()
        ShoeColor.objects.all().delete()
        SubImage.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        OrderStatus.objects.all().delete()
        Order.objects.all().delete()
        ProductOrder.objects.all().delete()

    def test_updateorderview_test(self):
        client = Client()

        header = {"HTTP_Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.6mlhvmw9MyBvInOVrhOnQNizB8iPI47xZ_2sC1gUcXs"}
        data = {
            "id" : 1,
            "quantity" : 2
        }
        response = client.post('/order/update', json.dumps(data), content_type = 'application/json', **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"pending_orders" : [
            {
                "id" : 1,
                "image" : "image",
                "name" : "test",
                "price" : 95000,
                "color" : "블랙",
                "size" : 220,
                "quantity" : 2
            }
        ]})

class DeleteOrderViewTest(TestCase):
    maxDiff = None
    
    def setUp(self):
        MainCategory.objects.create(id=1, name='신발')
        ShoeCategory.objects.create(id=1, main_category = MainCategory.objects.get(id=1), name='척 70')
        Detail.objects.create(id=1, name='test', main_detail='test', sub_detail='test', feature='test', feature_image='test')
        Size.objects.create(id=1, name=220)
        ColorFilter.objects.create(id=1, name='black')
        Color.objects.create(id=1, color_category=ColorFilter.objects.get(id=1),name='블랙')
        TypeFilter.objects.create(id=1, name='스니커즈')
        GenderSegmentation.objects.create(id=1, name='남녀공용')
        Shoe.objects.create(
            id=1,
            main_category = MainCategory.objects.get(id=1),
            shoe_category = ShoeCategory.objects.get(id=1),
            type_filter = TypeFilter.objects.get(id=1),
            detail = Detail.objects.get(id=1),
            gender_segmentation = GenderSegmentation.objects.get(id=1),
            price=95000.00
        )
        MainImage.objects.create(id=1, image='image')
        ShoeColor.objects.create(
            id=1,
            shoe = Shoe.objects.get(id=1),
            color = Color.objects.get(id=1),
            image = MainImage.objects.get(id=1)
        )
        ShoeColorSize.objects.create(id=1, shoecolor=ShoeColor.objects.get(id=1), size=Size.objects.get(id=1), quantity=2)
        SubImage.objects.create(id=1, image='image', is_hovered=True)
        Gender.objects.create(id=1, name='여성')
        User.objects.create(
            id = 1,
            email = 'test@test.com',
            password = 'a1234!dddd',
            phone_number = '01012341234',
            gender = Gender.objects.get(id=1),
            birth_date = '2020-07-28',
            name = 'test'
        )
        OrderStatus.objects.create(id=1, name="pending")
        Order.objects.create(id=1,user=User.objects.get(id=1), status = OrderStatus.objects.get(name="pending"))
        ProductOrder.objects.create(id=1, order = Order.objects.get(id=1), product=ShoeColorSize.objects.get(id=1), order_quantity=1)

    def tearDown(self):
        MainCategory.objects.all().delete()
        ShoeCategory.objects.all().delete()
        ColorFilter.objects.all().delete()
        Color.objects.all().delete()
        TypeFilter.objects.all().delete()
        GenderSegmentation.objects.all().delete()
        Detail.objects.all().delete()
        Shoe.objects.all().delete()
        MainImage.objects.all().delete()
        ShoeColor.objects.all().delete()
        SubImage.objects.all().delete()
        Gender.objects.all().delete()
        User.objects.all().delete()
        OrderStatus.objects.all().delete()
        Order.objects.all().delete()
        ProductOrder.objects.all().delete()

    def test_deleteorderview_test(self):
        client = Client()

        header = {"HTTP_Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.6mlhvmw9MyBvInOVrhOnQNizB8iPI47xZ_2sC1gUcXs"}
        response = client.post('/order/delete', content_type='application/json',**header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'pending_orders' : []})
