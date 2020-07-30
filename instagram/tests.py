from django.test import (
    TestCase,
    Client
)

from .models import Instagram

class InstagramViewTest(TestCase):
    
    def setUp(self):
        Instagram.objects.create(
            user               = 'user',
            user_profile_image = 'image',
            image              = 'image',
            text               = 'text'
        )

    def tearDown(self):
        Instagram.objects.all().delete()

    def test_instagramview_success(self):
        client = Client()
        response = client.get('/instagram?page=0&limit=8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            "posts" : [
                {
                    "id"                 : 1,
                    "user"               : "user",
                    "user_profile_image" : "image",
                    "image"              : "image",
                    "text"               : "text"
                }
            ]
        })

