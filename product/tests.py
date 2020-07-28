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
                                    main_category = MainCategory.objects.get(id=1))
        Detail.objects.create(
            name          = '척 70 시그니처',
            main_detail   = '척 테일러의 서명으로 완성된 컨버스 대표 아이콘',
            sub_detail    = '당대 최고의 디테일과 프리미엄 소재를 사용해 흠잡을 데 없는 장인정신으로 제작한 척 70은 지금도 컨버스 대표 아이콘으로서 그 명목이 이어져오고 있습니다. 편안하고 기분 좋은 패션을 완성하는 척 70은 패션 위크 런웨이와 도시 거리에서 자신의 스타일을 표현하고자 하는 사람들을 위한 아이템입니다. 필기체로 디자인된 척 시그니처 그래픽이 고급스러움과 클래식함을 더합니다',
            feature       = '가벼우면서도 견고한 프리미엄 코튼 소재 어퍼 , 전면의 척 테일러 시그니처 프린트 , 하루종일 편안한 착화감을 선사하는 강화된 쿠셔닝 , 프리미엄 빈티지 힐 패치',
            feature_image = 'http://tcakorea.speedgabia.com/converse/SU20/167699C.jpg'
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
            color_category = ColorFilter.objects.get(id = 1),
            name           = '블랙'
        )
        TypeFilter.objects.create(name='스니커즈')
        GenderSegmentation.objects.create(name='남녀공용')
        Shoe.objects.create(
            id                  = 1,
            main_category       = MainCategory.objects.get(id = 1),
            shoe_category       = ShoeCategory.objects.get(id = 1),
            type_filter         = TypeFilter.objects.get(id = 1),
            detail              = Detail.objects.get(id = 1),
            gender_segmentation = GenderSegmentation.objects.get(id = 1),
            price               = 95000
        )
        MainImage.objects.create(image='https://image.converse.co.kr/cmsstatic/product/167698C_167698C_pdp-primary.jpg?gallery=')
        ShoeColor.objects.create(
            shoe    = Shoe.objects.get(id=1),
            color   = Color.objects.get(id=1),
            image   = MainImage.objects.get(id=1)
        )
        ShoeColorSize.objects.bulk_create([
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=1), quantity = 1),
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=2), quantity = 1),
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=3), quantity = 1),
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=4), quantity = 1),
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=5), quantity = 1),
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=6), quantity = 1),
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=7), quantity = 1),
            ShoeColorSize(shoe = ShoeColor.objects.get(id=1), size = Size.objects.get(id=8), quantity = 1),
        ])
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
            ShoeColorSize.objects.all().delete()
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
                        "price": "95000.00",
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
        MainCategory.objects.create(id=1, name = '신발')
        ShoeCategory.objects.create(id=1, name = '척 70', main_category = MainCategory.objects.get(id=1))
        Detail.objects.create(
            id=1,
            name          = '척 70 핵트 패션',
            main_detail   = '척 70 핵트 패션',
            sub_detail    = '척 70 핵트 패션',
            feature       = '척 70 핵트 패션',
            feature_image = 'image'
        )

        ColorFilter.objects.bulk_create([
            ColorFilter(id=1,name = 'khaki'),
            ColorFilter(id=2,name = 'black')
        ])
        Size.objects.create(id=1, name=220)
        Color.objects.bulk_create([
            Color(id = 1,color_category = ColorFilter.objects.get(name='khaki'), name = '노마드카키'),
            Color(id = 2,color_category = ColorFilter.objects.get(name='black'), name = '블랙')
        ])
        TypeFilter.objects.create(name='스니커즈')
        GenderSegmentation.objects.create(name='남녀공용')

        Shoe.objects.create(
            id = 1,
            main_category       = MainCategory.objects.get(id = 1),
            shoe_category       = ShoeCategory.objects.get(id = 1),
            type_filter         = TypeFilter.objects.get(name='스니커즈'),
            detail              = Detail.objects.get(id = 1),
            gender_segmentation = GenderSegmentation.objects.get(name='남녀공용'),
            price               = 99000,
        )

        MainImage.objects.bulk_create([
            MainImage(id=1,image = "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery="),
            MainImage(id=2,image = "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=")
        ])

        ShoeColor.objects.bulk_create([
            ShoeColor(
                id      = 1,
                shoe    = Shoe.objects.get(id = 1),
                color   = Color.objects.get(id = 1),
                image   = MainImage.objects.get(id = 1)
            ),
            ShoeColor(
                id      = 2,
                shoe    = Shoe.objects.get(id = 1),
                color   = Color.objects.get(id = 2),
                image   = MainImage.objects.get(id = 2)
            )
        ])
        ShoeColorSize.objects.bulk_create([
            ShoeColorSize(id=1, shoecolor = ShoeColor.objects.get(id=1), size=Size.objects.get(id=1), quantity=1),
            ShoeColorSize(id=2, shoecolor = ShoeColor.objects.get(id=2), size=Size.objects.get(id=1), quantity=1)
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
            "filters" : {
                "gender_filters": [
                    "남녀공용"
                ],
                "color_filters": [
                    "khaki",
                    "black"
                ],
                "type_filters": [
                    "스니커즈"
                ],
                "size_filters": [
                    220
                ]
            },
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
                        "price"      : "99000.00",
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

class FilterView(TestCase):
    maxDiff = None

    def setUp(self):
        MainCategory.objects.create(id=1,name='신발')
        ShoeCategory.objects.create(id=1,name='allstar')
        TypeFilter.objects.create(id=1,name='스니커즈')
        ColorFilter.objects.create(id=1,name='indigo')
        Size.objects.create(id=1,name=220)
        GenderSegmentation.objects.create(id=1,name='여성')
        Detail.objects.create(
            id            = 1,
            name          = "척테일러 올스타 데인티 데님 데이즈",
            main_detail   = "척테일러",
            sub_detail    = "척테일러",
            feature       = "척테일러",
            feature_image = "test"
        )
        Shoe.objects.create(
            id                  = 1,
            main_category       = MainCategory.objects.get(id = 1),
            shoe_category       = ShoeCategory.objects.get(id = 1),
            type_filter         = TypeFilter.objects.get(id = 1),
            detail              = Detail.objects.get(id = 1),
            gender_segmentation = GenderSegmentation.objects.get(id = 1),
            price               = 55000
        )
        MainImage.objects.create(id=1, image="https://image.converse.co.kr/cmsstatic/product/567872C_567872C_pdp-primary.jpg?gallery=")
        Color.objects.create(id=1, color_category=ColorFilter.objects.get(id=1), name='indigo')
        ShoeColor.objects.create(id=1, shoe = Shoe.objects.get(id=1), color = Color.objects.get(id=1), image = MainImage.objects.get(id=1))
        ShoeColorSize.objects.create(shoecolor=ShoeColor.objects.get(id=1), size = Size.objects.get(id=1), quantity = 1)
        SubImage.objects.create(id=1, shoe_color = ShoeColor.objects.get(id=1), image = "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_3.jpg?browse=", is_hovered = True)

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
        ShoeColorSize.objects.all().delete()

    def test_filterview_success(self):
        client = Client()
        response = client.get('/product/filter?color=indigo&size=220&gender=여성&page=0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "filters": {
                "gender_filters": [
                    "여성"
                ],
                "color_filters": [
                    "indigo"
                ],
                "type_filters": [
                    "스니커즈"
                ],
                "size_filters": [
                    220
                ]
            },
            "products": [
                {
                    "product_detail": {
                        "id": 1,
                        "shoe__id": 1,
                        "name": "척테일러 올스타 데인티 데님 데이즈",
                        "price": "55000.00",
                        "main_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_pdp-primary.jpg?gallery=",
                        "sub_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_3.jpg?browse="
                    },
                    "color_list": [
                        {
                            "shoe_id": 1,
                            "color_filter": "indigo",
                            "main_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_pdp-primary.jpg?gallery=",
                            "sub_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_3.jpg?browse="
                        }
                    ]
                }
            ]
        })
