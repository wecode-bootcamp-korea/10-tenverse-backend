import jwt

from django.test import (
    TestCase,
    Client
)

from user.models import (
    User,
    Gender
)
from product.models import ShoeColorSize
from .models    import (
    OrderStatus,
    Order,
    ProductOrder
)
from utils      import login_required

class OrderViewTest(TestCase):
    maxDiff = None

    def setUp(self):
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
        user = {email : 'test@test.com', password : 'a1234!dddd'}
        login_response = client.post('/user/signin', json.dumps(user), content_type='application/json')
        access_token = login_response.json()['access_token']
        token = {'Authorization' : access_token}
        response = client.post('/order', )

