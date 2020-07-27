from django.test import (
    TestCase,
    Client
)

from .models import(
    MainCategory,
    ShoeCategory,
    Size,
    ColorFilter,
    Color,
    TypeFilter,
    GenderSegmentation,
    Detail,
    Shoe,
    ShoeSize,
    MainImage,
    ShoeColor,
    SubImage
)

class MainViewTest(TestCase):
    maxDiff = None

    def setUp(self):
        MainCategory.objects.create(name = '신발')
        ShoeCategory.objects.create(name = '척 70', main_category = MainCategory.objects.get(id=1))
        Detail.objects.create(
            name          = '척 70 핵트 패션',
            main_detail   = '척 70 핵트 패션',
            sub_detail    = '척 70 핵트 패션',
            feature       = '척 70 핵트 패션',
            feature_image = 'image'
        )
        ColorFilter.objects.bulk_create([
            ColorFilter(name = 'khaki'),
            ColorFilter(name = 'black')
        ])
        Color.objects.bulk_create([
            Color(color_category = ColorFilter.objects.get(id=1), name = '노마드카키'),
            Color(color_category = ColorFilter.objects.get(id=2), name = '블랙')
        ])
        TypeFilter.objects.create(name='스니커즈')
        GenderSegmentation.objects.create(name='남녀공용')

        Shoe.objects.create(
            main_category       = MainCategory.objects.get(id = 1),
            shoe_category       = ShoeCategory.objects.get(id = 1),
            type_filter         = TypeFilter.objects.get(id = 1),
            detail              = Detail.objects.get(id = 1),
            gender_segmentation = GenderSegmentation.objects.get(id = 1),
            price               = 99000,
        )

        MainImage.objects.bulk_create([
            MainImage(image = "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery="),
            MainImage(image = "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=")
        ])

        ShoeColor.objects.bulk_create([
            ShoeColor(
                shoe  = Shoe.objects.get(id = 1),
                color = Color.objects.get(id = 1),
                image = MainImage.objects.get(id = 1)
            ),
            ShoeColor(
                shoe  = Shoe.objects.get(id = 1),
                color = Color.objects.get(id = 2),
                image = MainImage.objects.get(id = 2)
            )
        ])

        SubImage.objects.bulk_create([
            SubImage(
                shoe_color = ShoeColor.objects.get(id = 1),
                image      = "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse=",
                is_hover   = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id=2),
                image       = "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse=",
                is_hover    = True
            )
        ])

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

    def test_mainview_success(self):
        
        client = Client()
        response = client.get('/product')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "products" : [
                {
                    "product_detail" : {
                        "id"         : 1,
                        "shoe__id"   : 1,
                        "name"       : "척 70 핵트 패션",
                        "price"      : 99000,
                        "main_image" : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                        "sub_image"  : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="
                    },
                    "color_list": [
                        {
                            "shoe_id"       : 1,
                            "color_filter"  : "khaki"
                        },
                        {
                            "shoe_id"       : 2,
                            "color_filter"  : "black"
                        }
                    ]
                },
                {
                    "product_detail": {
                        "id"         : 2,
                        "shoe__id"   : 1,
                        "name"       : "척 70 핵트 패션",
                        "price"      : 99000,
                        "main_image" : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=",
                        "sub_image"  : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse="
                    },
                    "color_list": [
                        {
                            "shoe_id"      : 1,
                            "color_filter" : "khaki"
                        },
                        {
                            "shoe_id"      : 2,
                            "color_filter" : "black"
                            }
                    ]
                }
                ]})
