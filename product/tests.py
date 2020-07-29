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

'''class MainPageViewTest(TestCase):
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
                "price": 109000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/565829C_565829C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/565829C_565829C_03.jpg?browse="
            },
            {
                "id": 2,
                "name": "척테일러 올스타 리프트 캔버스",
                "price": 75000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/21553/560251C_560251C_primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/560251C_560251C_03.jpg?browse="
            },
            {
                "id": 3,
                "name": "척테일러 올스타 리프트 캔버스",
                "price": 75000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/560250C_560250C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/560250C_560250C_03.jpg?browse="
            },
            {
                "id": 4,
                "name": "척테일러 올스타 리프트 캔버스",
                "price": 79000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_03.jpg?browse="
            }
        ],
        "jack_purcell": [
            {
                "id": 5,
                "name": "잭퍼셀 컬러블록",
                "price": 89000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168976C_168976C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168976C_168976C_03.jpg?browse="
            },
            {
                "id": 6,
                "name": "척 70 핵트 패션",
                "price": 99000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse="
            }
        ],
        "pro_leather": [
            {
                "id": 7,
                "name": "잭퍼셀 트레일 투 코브",
                "price": 85000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168140C_168140C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168140C_168140C_03.jpg?browse="
            },
            {
                "id": 8,
                "name": "잭퍼셀 샤이니 레더",
                "price": 95000,
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
                            "price"      : 99000,
                            "main_image" : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_pdp-primary.jpg?gallery=",
                            "sub_image"  : "https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse=",
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
                    }},
                    {
                        "product_detail": {
                            "id"         : 2,
                            "shoe__id"   : 1,
                            "name"       : "척 70 핵트 패션",
                            "price"      : 99000,
                            "main_image" : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_pdp-primary.jpg?gallery=",
                            "sub_image"  : "https://image.converse.co.kr/cmsstatic/product/168696C_168696C_03.jpg?browse=",
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
                }]})
'''
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
        ShoeColorSize.objects.bulk_create([
            ShoeColorSize(shoecolor=ShoeColor.objects.get(id=1), size=Size.objects.get(name='220'), quantity = 1),
            ShoeColorSize(shoecolor=ShoeColor.objects.get(id=2), size=Size.objects.get(name='220'), quantity = 1)
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
        ShoeColorSize.objects.all().delete()
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
                "name": "원스타 프로 피그 스킨",
                "price": 99000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168654C_168654C_03.jpg?browse=",
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
        }},
        {
            "product_detail": {
                "id": 2,
                "name": "원스타 프로 피그 스킨",
                "price": 99000,
                "main_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_pdp-primary.jpg?gallery=",
                "sub_image": "https://image.converse.co.kr/cmsstatic/product/168655C_168655C_03.jpg?browse=",
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
    }]})

