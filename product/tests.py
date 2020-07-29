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
        MainCategory.objects.create(id=1, name='신발')
        ShoeCategory.objects.bulk_create([
            ShoeCategory(id=1,name='척 70', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(id=2,name='척테일러 올스타', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(id=3,name='올스타', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(id=4,name='잭퍼셀', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(id=5,name='프로레더', main_category = MainCategory.objects.get(id=1))
        ])
        Detail.objects.bulk_create([
            Detail(
                id=1,
                name          = '척테일러 올스타 리프트 EVA',
                main_detail   = '척테일러 올스타 리프트 EVA',
                sub_detail    = '척테일러 올스타 리프트 EVA',
                feature       = '척테일러 올스타 리프트 EVA',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                id=2,
                name          = '척테일러 올스타 리프트 캔버스',
                main_detail   = '척테일러 올스타 리프트 캔버스',
                sub_detail    = '척테일러 올스타 리프트 캔버스',
                feature       = '척테일러 올스타 리프트 캔버스',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                id=3,
                name          = '잭퍼셀 컬러블록',
                main_detail   = '잭퍼셀 컬러블록',
                sub_detail    = '잭퍼셀 컬러블록',
                feature       = '잭퍼셀 컬러블록',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                id=4,
                name          = '척 70 핵트 패션',
                main_detail   = '척 70 핵트 패션',
                sub_detail    = '척 70 핵트 패션',
                feature       = '척 70 핵트 패션',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                id=5,
                name          = '잭퍼셀 트레일 투 코브',
                main_detail   = '잭퍼셀 트레일 투 코브',
                sub_detail    = '잭퍼셀 트레일 투 코브',
                feature       = '잭퍼셀 트레일 투 코브',
                feature_image = 'image',
                is_main       = True
            ),
            Detail(
                id=6,
                name          = '잭퍼셀 샤이니 레더',
                main_detail   = '잭퍼셀 샤이니 레더',
                sub_detail    = '잭퍼셀 샤이니 레더',
                feature       = '잭퍼셀 샤이니 레더',
                feature_image = 'image',
                is_main       = True
            )
        ])

        ColorFilter.objects.bulk_create([
            ColorFilter(id=1,name = 'black'),
            ColorFilter(id=2,name = 'kahki'),
            ColorFilter(id=3,name = 'white')
        ])
        Size.objects.create(id=1, name=220)
        Color.objects.bulk_create([
            Color(id=1,color_category = ColorFilter.objects.get(name='black'),name = '블랙'),
            Color(id=2,color_category = ColorFilter.objects.get(name='kahki'),name = '노마드카키'),
            Color(id=3,color_category = ColorFilter.objects.get(name='white'),name = '화이트'),
            Color(id=4,color_category = ColorFilter.objects.get(name='white'),name = '페일퍼티')])

        TypeFilter.objects.create(name='스니커즈')
        
        GenderSegmentation.objects.create(name='남녀공용')

        Shoe.objects.bulk_create([
            Shoe(
                id=1,
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 1),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 109000
            ),
            Shoe(
                id=2,
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 2),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 75000
            ),
            Shoe(
                id=3,
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 2),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 79000
            ),
            Shoe(
                id=4,
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 3),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 89000
            ),
            Shoe(
                id=5,
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 4),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 99000
            ),
            Shoe(
                id=6,
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 5),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 85000
            ),
            Shoe(
                id=7,
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(name = '스니커즈'),
                detail              = Detail.objects.get(id = 6),
                gender_segmentation = GenderSegmentation.objects.get(name = '남녀공용'),
                price               = 95000
            )
        ])

        MainImage.objects.bulk_create([
            MainImage(id=1,image='https://image.converse.co.kr/cmsstatic/product/565829C_565829C_pdp-primary.jpg?gallery='),
            MainImage(id=2,image='https://image.converse.co.kr/cmsstatic/product/21553/560251C_560251C_primary.jpg?gallery='),
            MainImage(id=3,image='https://image.converse.co.kr/cmsstatic/product/560250C_560250C_pdp-primary.jpg?gallery='),
            MainImage(id=4,image='https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_pdp-primary.jpg?gallery='),
            MainImage(id=5,image='https://image.converse.co.kr/cmsstatic/product/168976C_168976C_pdp-primary.jpg?gallery='),
            MainImage(id=6,image='https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery='),
            MainImage(id=7,image='https://image.converse.co.kr/cmsstatic/product/168140C_168140C_pdp-primary.jpg?gallery='),
            MainImage(id=8,image='https://image.converse.co.kr/cmsstatic/product/168135C_168135C_pdp-primary.jpg?gallery=')
        ])

        ShoeColor.objects.bulk_create([
            ShoeColor(id=1,shoe = Shoe.objects.get(id=1),color = Color.objects.get(id=4), image = MainImage.objects.get(id=1)),
            ShoeColor(id=2,shoe = Shoe.objects.get(id=2),color = Color.objects.get(id=3), image = MainImage.objects.get(id=2)),
            ShoeColor(id=3,shoe = Shoe.objects.get(id=2),color = Color.objects.get(id=1), image = MainImage.objects.get(id=3)),
            ShoeColor(id=4,shoe = Shoe.objects.get(id=3),color = Color.objects.get(id=3), image = MainImage.objects.get(id=4)),
            ShoeColor(id=5,shoe = Shoe.objects.get(id=4),color = Color.objects.get(id=2), image = MainImage.objects.get(id=5)),
            ShoeColor(id=6,shoe = Shoe.objects.get(id=5),color = Color.objects.get(id=2), image = MainImage.objects.get(id=6)),
            ShoeColor(id=7,shoe = Shoe.objects.get(id=6),color = Color.objects.get(id=3), image = MainImage.objects.get(id=7)),
            ShoeColor(id=8,shoe = Shoe.objects.get(id=7),color = Color.objects.get(id=3), image = MainImage.objects.get(id=8))
        ])
        SubImage.objects.bulk_create([
            SubImage(
                shoe_color = ShoeColor.objects.get(id = 1),
                image      = "https://image.converse.co.kr/cmsstatic/product/565829C_565829C_03.jpg?browse=",
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
                        "price": 55000,
                        "main_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_pdp-primary.jpg?gallery=",
                        "sub_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_3.jpg?browse=",
                        "color_list": [
                        {
                            "shoe_id": 1,
                            "color_filter": "indigo",
                            "main_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_pdp-primary.jpg?gallery=",
                            "sub_image": "https://image.converse.co.kr/cmsstatic/product/567872C_567872C_3.jpg?browse="
                        }
                    ]
                }
            }
            ]})
