import json

from .models     import (
    Gender,
    User
)
from django.test import (
    TestCase,
    Client,
)

client = Client()
class SignUpTest(TestCase):
    def setUp(self):
        Gender.objects.create(name='남성')

    def tearDown(self):
        User.objects.all().delete()

    def test_post_view(self):
        user = {
            'email'        : 'test11@test.com',
            'password'     : 'test1!dddd',
            'name'         : 'test10',
            'phone_number' : '01012341234',
            'gender'       : '남성',
            'birth_date'   : '2020-07-22'
        }
        response = client.post('/user/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "SUCCESS"})

