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
            Color(color_category = ColorFilter.objects.get(name='khaki'), name = '노마드카키'),
            Color(color_category = ColorFilter.objects.get(name='black'), name = '블랙')
        ])
        TypeFilter.objects.create(name='스니커즈')
        GenderSegmentation.objects.create(name='남녀공용')

        Shoe.objects.create(
            main_category       = MainCategory.objects.get(id = 1),
            shoe_category       = ShoeCategory.objects.get(id = 1),
            type_filter         = TypeFilter.objects.get(name='스니커즈'),
            detail              = Detail.objects.get(id = 1),
            gender_segmentation = GenderSegmentation.objects.get(name='남녀공용'),
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
                is_hovered = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id=2),
                image       = "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse=",
                is_hovered  = True
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
        response = client.get('/product?page=0')
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
                            "color_filter"  : "khaki",
                            "main_image"    : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                            "sub_image"     : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="
                        },
                        {
                            "shoe_id"       : 2,
                            "color_filter"  : "black",
                            "main_image"    : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=",
                            "sub_image"     : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse="
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
                            "color_filter" : "khaki",
                            "main_image"   : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                            "sub_image"    : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="
                        },
                        {
                            "shoe_id"       : 2,
                            "color_filter"  : "black",
                            "main_image"    : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=",
                            "sub_image"     : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse="
                        }
                    ]
                }
                ]})

class CategoryViewTest(TestCase):
    maxDiff = None 

    def setUp(self):
        Size.objects.bulk_create([
            Size(name=220),
            Size(name=225),
            Size(name=230),
            Size(name=235),
            Size(name=240),
            Size(name=245),
            Size(name=250),
            Size(name=255),
            Size(name=260),
            Size(name=265),
            Size(name=270),
            Size(name=275),
            Size(name=280),
            Size(name=285),
            Size(name=290),
            Size(name=295),
            Size(name=300)
        ])
        
        ColorFilter.objects.bulk_create([
            ColorFilter(name='black'),
            ColorFilter(name='blue'),
            ColorFilter(name='green'),
            ColorFilter(name='indigo'),
            ColorFilter(name='purple'),
            ColorFilter(name='brown'),
            ColorFilter(name='gray'),
            ColorFilter(name='khaki'),
            ColorFilter(name='beige'),
            ColorFilter(name='red'),
            ColorFilter(name='orange'),
            ColorFilter(name='pink'),
            ColorFilter(name='yellow'),
            ColorFilter(name='white'),
        ])

        TypeFilter.objects.bulk_create([
            TypeFilter(name='뮬'),
            TypeFilter(name='샌들&뮬'),
            TypeFilter(name='스니커즈')
        ])

        GenderSegmentation.objects.bulk_create([
            GenderSegmentation(name='여성'),
            GenderSegmentation(name='남성'),
            GenderSegmentation(name='남녀공용')
        ])

    def tearDown(self):
        Size.objects.all().delete()
        ColorFilter.objects.all().delete()
        TypeFilter.objects.all().delete()
        GenderSegmentation.objects.all().delete()

    def test_categoryfilter_success(self):
        client = Client()
        response = client.get('/product/category')
        self.assertEqual(response.status_code, 200),
        self.assertEqual(response.json(), {
            "filters": {
                "gender_filters": [
                    "여성",
                    "남성",
                    "남녀공용"
                ],
                "color_filters": [
                    "black",
                    "blue",
                    "green",
                    "indigo",
                    "purple",
                    "brown",
                    "gray",
                    "khaki",
                    "beige",
                    "red",
                    "orange",
                    "pink",
                    "yellow",
                    "white"
                ],
                "type_filters": [
                    "뮬",
                    "샌들&뮬",
                    "스니커즈"
                ],
                "size_filters": [
                    220,
                    225,
                    230,
                    235,
                    240,
                    245,
                    250,
                    255,
                    260,
                    265,
                    270,
                    275,
                    280,
                    285,
                    290,
                    295,
                    300
                ]
            }
        })

class ShoeCategoryViewTest(TestCase):
    maxDiff = None
    
    def setUp(self):
        MainCategory.objects.create(name='신발')
        ShoeCategory.objects.create(name='onestar', main_category = MainCategory.objects.get(name='신발'))
        Size.objects.create(name='220')
        ColorFilter.objects.bulk_create([
            ColorFilter(name='green'),
            ColorFilter(name='indigo')
        ])
        TypeFilter.objects.create(name='스니커즈')
        GenderSegmentation.objects.create(name='남녀공용')
        Detail.objects.create(
            name = '원스타 프로 피그 스킨',
            main_detail = '원스타 프로 피그 스킨',
            sub_detail = '원스타 프로 피그 스킨',
            feature = '원스타 프로 피그 스킨',
            feature_image = 'image'
        )
        Shoe.objects.create(
            id = 1,
            main_category = MainCategory.objects.get(name='신발'),
            shoe_category = ShoeCategory.objects.get(name='onestar'),
            type_filter = TypeFilter.objects.get(name='스니커즈'),
            detail = Detail.objects.get(name='원스타 프로 피그 스킨'),
            gender_segmentation = GenderSegmentation.objects.get(name='남녀공용'),
            price = 99000
        )
        ShoeSize.objects.create(shoe=Shoe.objects.get(id=1), size=Size.objects.get(name='220'))
        Color.objects.bulk_create([
            Color(color_category = ColorFilter.objects.get(name='green'), name = 'green'),
            Color(color_category = ColorFilter.objects.get(name='indigo'), name = 'indigo')
        ])
        MainImage.objects.bulk_create([
            MainImage(id=1, image = "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_pdp-primary.jpg?gallery="),
            MainImage(id=2, image = "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_pdp-primary.jpg?gallery=")
        ])
        ShoeColor.objects.bulk_create([
            ShoeColor(id = 1, shoe = Shoe.objects.get(id=1), color = Color.objects.get(name='green'), image = MainImage.objects.get(id=1)),
            ShoeColor(id = 2, shoe = Shoe.objects.get(id=1), color = Color.objects.get(name='indigo'), image = MainImage.objects.get(id=2))
        ])
        SubImage.objects.bulk_create([
            SubImage(shoe_color = ShoeColor.objects.get(id=1), image = "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_03.jpg?browse=", is_hovered = True),
            SubImage(shoe_color = ShoeColor.objects.get(id=2), image = "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_03.jpg?browse=", is_hovered = True)
        ])

    def tearDown(self):
        MainCategory.objects.all().delete()
        ShoeCategory.objects.all().delete()
        Size.objects.all().delete()
        ColorFilter.objects.all().delete()
        TypeFilter.objects.all().delete()
        GenderSegmentation.objects.all().delete()
        Detail.objects.all().delete()
        Shoe.objects.all().delete()
        ShoeSize.objects.all().delete()
        Color.objects.all().delete()
        MainImage.objects.all().delete()
        ShoeColor.objects.all().delete()
        SubImage.objects.all().delete()

    def test_shoecategoryview_success(self):
        client = Client()
        response = client.get('/product/onestar?page=0')
        self.assertEqual(response.status_code, 200),
        self.assertEqual(response.json(),{
    "filters": {
        "genders": [
            "남녀공용"
        ],
        "colors": [
            "green",
            "indigo"
        ],
        "types": [
            "스니커즈"
        ],
        "sizes": [
            220
        ]
    },
    "products": [
        {
            "product_detail": {
                "id": 1,
                "shoe__id": 1,
                "name": "원스타 프로 피그 스킨",
                "price": 99000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_03.jpg?browse="
            },
            "color_list": [
                {
                    "shoe_id": 1,
                    "color_filter": "green",
                    "main_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_pdp-primary.jpg?gallery=",
                    "sub_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_03.jpg?browse="
                },
                {
                    "shoe_id": 2,
                    "color_filter": "indigo",
                    "main_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_pdp-primary.jpg?gallery=",
                    "sub_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_03.jpg?browse="
                }
            ]
        },
        {
            "product_detail": {
                "id": 2,
                "shoe__id": 1,
                "name": "원스타 프로 피그 스킨",
                "price": 99000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_03.jpg?browse="
            },
            "color_list": [
                {
                    "shoe_id": 1,
                    "color_filter": "green",
                    "main_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_pdp-primary.jpg?gallery=",
                    "sub_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_03.jpg?browse="
                },
                {
                    "shoe_id": 2,
                    "color_filter": "indigo",
                    "main_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_pdp-primary.jpg?gallery=",
                    "sub_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_03.jpg?browse="
                }
            ]
        }
    ]})


