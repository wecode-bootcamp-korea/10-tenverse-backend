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
    ShoeColorSize,
    MainImage,
    ShoeColor,
    SubImage
)

class MainPageViewTest(TestCase):
    maxDiff = None

    def setUp(self):
        MainCategory.objects.create(name='신발')
        ShoeCategory.objects.bulk_create([
            ShoeCategory(name='척 70', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(name='척테일러 올스타', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(name='올스타', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(name='잭퍼셀', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(name='프로레더', main_category = MainCategory.objects.get(id=1))
        ])
        Detail.objects.bulk_create([
            Detail(
                name          = '척테일러 올스타 리프트 EVA',
                main_detail   = '척테일러 올스타 리프트 EVA',
                sub_detail    = '척테일러 올스타 리프트 EVA',
                feature       = '척테일러 올스타 리프트 EVA',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                name          = '척테일러 올스타 리프트 캔버스',
                main_detail   = '척테일러 올스타 리프트 캔버스',
                sub_detail    = '척테일러 올스타 리프트 캔버스',
                feature       = '척테일러 올스타 리프트 캔버스',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                name          = '잭퍼셀 컬러블록',
                main_detail   = '잭퍼셀 컬러블록',
                sub_detail    = '잭퍼셀 컬러블록',
                feature       = '잭퍼셀 컬러블록',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                name          = '척 70 핵트 패션',
                main_detail   = '척 70 핵트 패션',
                sub_detail    = '척 70 핵트 패션',
                feature       = '척 70 핵트 패션',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                name          = '잭퍼셀 트레일 투 코브',
                main_detail   = '잭퍼셀 트레일 투 코브',
                sub_detail    = '잭퍼셀 트레일 투 코브',
                feature       = '잭퍼셀 트레일 투 코브',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                name          = '잭퍼셀 샤이니 레더',
                main_detail   = '잭퍼셀 샤이니 레더',
                sub_detail    = '잭퍼셀 샤이니 레더',
                feature       = '잭퍼셀 샤이니 레더',
                feature_image = 'image',
                is_main       = True
            )
        ])

        ColorFilter.objects.bulk_create([
            ColorFilter( name = 'black'),
            ColorFilter( name = 'kahki'),
            ColorFilter( name = 'white')
        ])

        Color.objects.bulk_create([
            Color(color_category = ColorFilter.objects.get(name='black'),name = '블랙'),
            Color(color_category = ColorFilter.objects.get(name='kahki'),name = '노마드카키'),
            Color(color_category = ColorFilter.objects.get(name='white'),name = '화이트'),
            Color(color_category = ColorFilter.objects.get(name='white'),name = '페일퍼티')])

        TypeFilter.objects.create(name='스니커즈')
        
        GenderSegmentation.objects.create(name='남녀공용')

        Shoe.objects.bulk_create([
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 1),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 109000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 2),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 75000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 2),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 79000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 3),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 89000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 4),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 99000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 5),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 85000),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 6),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 95000
            )
        ])

        MainImage.objects.bulk_create([
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/565829C_565829C_pdp-primary.jpg?gallery='),
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/21553/560251C_560251C_primary.jpg?gallery='),
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/560250C_560250C_pdp-primary.jpg?gallery='),
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_pdp-primary.jpg?gallery='),
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/168976C_168976C_pdp-primary.jpg?gallery='),
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery='),
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/168140C_168140C_pdp-primary.jpg?gallery='),
            MainImage(image='https://image.converse.co.kr/cmsstatic/product/168135C_168135C_pdp-primary.jpg?gallery=')
        ])

        ShoeColor.objects.bulk_create([
            ShoeColor(shoe = Shoe.objects.get(id=1),color = Color.objects.get(id=4), image = MainImage.objects.get(id=1)),
            ShoeColor(shoe = Shoe.objects.get(id=2),color = Color.objects.get(id=3), image = MainImage.objects.get(id=2)),
            ShoeColor(shoe = Shoe.objects.get(id=2),color = Color.objects.get(id=1), image = MainImage.objects.get(id=3)),
            ShoeColor(shoe = Shoe.objects.get(id=3),color = Color.objects.get(id=3), image = MainImage.objects.get(id=4)),
            ShoeColor(shoe = Shoe.objects.get(id=4),color = Color.objects.get(id=2), image = MainImage.objects.get(id=5)),
            ShoeColor(shoe = Shoe.objects.get(id=5),color = Color.objects.get(id=2), image = MainImage.objects.get(id=6)),
            ShoeColor(shoe = Shoe.objects.get(id=6),color = Color.objects.get(id=3), image = MainImage.objects.get(id=7)),
            ShoeColor(shoe = Shoe.objects.get(id=7),color = Color.objects.get(id=3), image = MainImage.objects.get(id=8))
        ])

        SubImage.objects.bulk_create([
            SubImage(
                shoe_color = ShoeColor.objects.get(id = 1),
                image      = 'https://image.converse.co.kr/cmsstatic/product/565829C_565829C_03.jpg?browse=',
                is_hovered = True
            ),
            SubImage(
                shoe_color = ShoeColor.objects.get(id = 2),
                image      = 'https://image.converse.co.kr/cmsstatic/product/560251C_560251C_03.jpg?browse=',
                is_hovered  = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 3),
                image       ='https://image.converse.co.kr/cmsstatic/product/560250C_560250C_03.jpg?browse=',
                is_hovered   = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 4),
                image       ='https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_03.jpg?browse=',
                is_hovered  = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 5),
                image       ='https://image.converse.co.kr/cmsstatic/product/168976C_168976C_03.jpg?browse=',
                is_hovered  = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 6),
                image       ='https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse=',
                is_hovered  = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 7),
                image       ='https://image.converse.co.kr/cmsstatic/product/168140C_168140C_03.jpg?browse=',
                is_hovered  = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 8),
                image       ='https://image.converse.co.kr/cmsstatic/product/168135C_168135C_03.jpg?browse=',
                is_hovered  = True
            )])

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

    def test_mainpageview_success(self):
        
        client = Client()
        response = client.get('/product/mainpage')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
    "products": {
        "women_collection": [
            {
                "id": 1,
                "name": "척테일러 올스타 리프트 EVA",
                "price": "109000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/565829C_565829C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/565829C_565829C_03.jpg?browse="
            },
            {
                "id": 2,
                "name": "척테일러 올스타 리프트 캔버스",
                "price": "75000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/21553/560251C_560251C_primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/560251C_560251C_03.jpg?browse="
            },
            {
                "id": 3,
                "name": "척테일러 올스타 리프트 캔버스",
                "price": "75000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/560250C_560250C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/560250C_560250C_03.jpg?browse="
            },
            {
                "id": 4,
                "name": "척테일러 올스타 리프트 캔버스",
                "price": "79000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_03.jpg?browse="
            }
        ],
        "jack_purcell": [
            {
                "id": 5,
                "name": "잭퍼셀 컬러블록",
                "price": "89000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168976C_168976C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168976C_168976C_03.jpg?browse="
            },
            {
                "id": 6,
                "name": "척 70 핵트 패션",
                "price": "99000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="
            }
        ],
        "pro_leather": [
            {
                "id": 7,
                "name": "잭퍼셀 트레일 투 코브",
                "price": "85000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168140C_168140C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168140C_168140C_03.jpg?browse="
            },
            {
                "id": 8,
                "name": "잭퍼셀 샤이니 레더",
                "price": "95000.00",
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168135C_168135C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168135C_168135C_03.jpg?browse="
            }
        ]
    }
})

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
            )])
        
        SubImage.objects.bulk_create([
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 1),
                image       = "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse=",
                is_hovered  = True
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
            response = client.get('/product')
            products = list(ShoeColor.objects.all().values('shoe__price'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "products" : [
                    {
                        "product_detail" : {
                            "id"         : 1,
                            "shoe__id"   : 1,
                            "name"       : "척 70 핵트 패션",
                            "price"      : "99000.00",
                            "main_image" : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                            "sub_image"  : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="
                        },
                        "color_list": [
                            {
                                "shoe_id"       : 1,
                                "color_filter"  : "khaki",
                                "main_image"    : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                                "sub_image"     : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="         },
                            {
                                "shoe_id"       : 2,
                                "color_filter"  : "black",
                                "main_image"    : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=",
                                "sub_image" : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse="
                            }
                        ]
                    },
                    {
                        "product_detail": {
                            "id"         : 2,
                            "shoe__id"   : 1,
                            "name"       : "척 70 핵트 패션",
                            "price"      : "99000.00",
                            "main_image" : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=",
                            "sub_image"  : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse="
                        },
                        "color_list": [
                            {
                                "shoe_id"       : 1,
                                "color_filter"  : "khaki",
                                "main_image"    : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                                "sub_image"     : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="         },
                            {
                                "shoe_id"       : 2,
                                "color_filter"  : "black",
                                "main_image"    : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=",
                                "sub_image" : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse="
                            }
                        ]
                    }
                ]})
