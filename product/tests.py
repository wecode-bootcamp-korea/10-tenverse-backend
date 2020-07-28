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

class DetailViewTest(TestCase):
    
    def setUp(self):
        MainCategory.objects.create(name='신발')
        ShoeCategory.objects.create(name='척 70', 
                                    main_category = MainCategory.objects.get(id=1)
                                   )
        Detail.objects.create(name='척 70 시그니처', 
                              main_detail='척 테일러의 서명으로 완성된 컨버스 대표 아이콘',
                              sub_detail='당대 최고의 디테일과 프리미엄 소재를 사용해 흠잡을 데 없는 장인정신으로 제작한 척 70은 지금도 컨버스 대표 아이콘으로서 그 명목이 이어져오고 있습니다. 편안하고 기분 좋은 패션을 완성하는 척 70은 패션 위크 런웨이와 도시 거리에서 자신의 스타일을 표현하고자 하는 사람들을 위한 아이템입니다. 필기체로 디자인된 척 시그니처 그래픽이 고급스러움과 클래식함을 더합니다',
                              feature='가벼우면서도 견고한 프리미엄 코튼 소재 어퍼 , 전면의 척 테일러 시그니처 프린트 , 하루종일 편안한 착화감을 선사하는 강화된 쿠셔닝 , 프리미엄 빈티지 힐 패치',
                              feature_image='http://tcakorea.speedgabia.com/converse/SU20/167699C.jpg'
                             )
        Size.objects.bulk_create([
            Size(name=220),
            Size(name=230),
            Size(name=240),
            Size(name=250),
            Size(name=260),
            Size(name=270),
            Size(name=280),
            Size(name=290)
        ])

        ColorFilter.objects.create(name='black')
        Color.objects.cerate(
            color_category = ColorFilter.objects.get(id=1),
            name = '블랙'
        )
        TypeFilter.objects.create(name='스니커즈')
        GenderSegmentation.objects.create(name='남녀공용')
        Shoe.objects.create(
            main_category = MainCategory.objects.get(id=1),
            shoe_category = ShoeCategory.objects.get(id=1),
            type_filter = TypeFilter.objects.get(id=1),
            detail = Detail.objects.get(id=1),
            gender_segmentation = GenderSegmentation.objects.get(id=1),
            price = 95000
        )
        ShoeSize.objects.bulk_create([
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=1)),
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=2)),
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=3)),
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=4)),
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=5)),
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=6)),
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=7)),
            ShoeSize(shoe = Shoe.objects.get(id=1), size = Size.objects.get(id=8)),
        ])
        MainImage.objects.create(image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_pdp-primary.jpg?gallery=')
        ShoeColor.objects.create(
            shoe = Shoe.objects.get(id=1),
            color = Color.objects.get(id=1),
            image = MainImage.objects.get(id=1)
        )
        SubImage.objects.bulk_create([
            SubImage(shoe_color = ShoeColor.objects.get(id=1), image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_primary.jpg?gallery='),
            SubImage(shoe_color = ShoeColor.objects.get(id=1), image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_2.jpg?browse='),
            SubImage(shoe_color = ShoeColor.objects.get(id=1), image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_3.jpg?browse='),
            SubImage(shoe_color = ShoeColor.objects.get(id=1), image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_4.jpg?browse='),
            SubImage(shoe_color = ShoeColor.objects.get(id=1), image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_5.jpg?browse='),
            SubImage(shoe_color = ShoeColor.objects.get(id=1), image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_6.jpg?browse='),
        ])

        def tearDown(self):
            MainCategory.objects.all().delete()
            ShoeCategory.objects.all().delete()
            Size.objects.all().delete()
            ColorFilter.objects.all().delete()
            Color.objects.all().delete()
            TypeFilter.objects.all().delete()
            GenderSegmentation.objects.all().delete()
            Detail.objects.all().delete()
            Shoe.objects.all().delete()
            ShoeSize.objects.all().delete()
            MainImage.objects.all().delete()
            ShoeColor.objects.all().delete()
            SubImage.objects.all().delete()

        def test_detailview_success(self):
            client = Client()
            response = client.get('/product/detail/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
    "product": [
        {
            "id": 1,
            "name": "척 70 시그니처",
            "price": 95000,
            "gender": "남녀공용",
            "color_name": "블랙",
            "main_detail": "척 테일러의 서명으로 완성된 컨버스 대표 아이콘",
            "sub_detail": "당대 최고의 디테일과 프리미엄 소재를 사용해 흠잡을 데 없는 장인정신으로 제작한 척 70은 지금도 컨버스 대표 아이콘으로서 그 명목이 이어져오고 있습니다. 편안하고 기분 좋은 패션을 완성하는 척 70은 패션 위크 런웨이와 도시 거리에서 자신의 스타일을 표현하고자 하는 사람들을 위한 아이템입니다. 필기체로 디자인된 척 시그니처 그래픽이 고급스러움과 클래식함을 더합니다.",
            "features": "가벼우면서도 견고한 프리미엄 코튼 소재 어퍼 , 전면의 척 테일러 시그니처 프린트 , 하루종일 편안한 착화감을 선사하는 강화된 쿠셔닝 , 프리미엄 빈티지 힐 패치",
            "feature_image": "http://tcakorea.speedgabia.com/converse/SU20/167699C.jpg",
            "main_image": "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_pdp-primary.jpg?gallery="
        },
        {
            "sub_image": [
                "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_primary.jpg?gallery=",
                "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_2.jpg?browse=",
                "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_3.jpg?browse=",
                "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_4.jpg?browse=",
                "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_5.jpg?browse=",
                "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_6.jpg?browse="
            ],
            "color_list": [
                {
                    "id": 1,
                    "main_image": "https://image.converse.co.kr/cmsstatic/product/167698C_167698C_pdp-primary.jpg?gallery="
                },
                {
                    "id": 219,
                    "main_image": "https://image.converse.co.kr/cmsstatic/product/167699C_167699C_pdp-primary.jpg?gallery="
                }
            ],
            "size_list": [
                220,
                230,
                240,
                250,
                260,
                270,
                280,
                290
            ]
        }
    ]
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

