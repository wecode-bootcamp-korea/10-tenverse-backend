import jwt

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
        Detail.objects.create(id=1, main_detail='test', sub_detail='test', feature='test', 'feature_image'='test')
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
        Gender.objects.all().delete()
        User.objects.all().delete()
        OrderStatus.objects.all().delete()

    def test_orderview_success(self):
        client = Client()
        token = {"HTTP_Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.6mlhvmw9MyBvInOVrhOnQNizB8iPI47xZ_2sC1gUcXs"}
        order = {
            'product' : 1,
            'size' : 220,
            'quantity' : 1
        }
        response = client.post('/order', json.dumps(order), **token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})
