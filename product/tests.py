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

class MainPageViewTest(TestCase):
    
    def setUp(self):
        MainCategory.objects.create(name='신발')
        ShoeCategory.objects.bulk_create([
            ShoeCategory(name='척 70', main_category = MainCategory.objects.get(id=1)),
            ShoeCategory(name='척테일러', main_category = MainCategory.objects.get(id=1)),
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
                is_main = True
            ),
            Detail(
                name          = '척테일러 올스타 리프트 캔버스',
                main_detail   = '척테일러 올스타 리프트 캔버스',
                sub_detail    = '척테일러 올스타 리프트 캔버스',
                feature       = '척테일러 올스타 리프트 캔버스',
                feature_image = 'image',
                is_main = True
            ),
            Detail(
                name          = '잭퍼셀 컬러블록',
                main_detail   = '잭퍼셀 컬러블록',
                sub_detail    = '잭퍼셀 컬러블록',
                feature       = '잭퍼셀 컬러블록',
                feature_image = 'image',
                is_main = True
            ),
            Detail(
                name          = '척 70 핵트 패션',
                main_detail   = '척 70 핵트 패션',
                sub_detail    = '척 70 핵트 패션',
                feature       = '척 70 핵트 패션',
                feature_image = 'image',
                is_main = True
            ),
            Detail(
                name          = '잭퍼셀 트레일 투 코브',
                main_detail   = '잭퍼셀 트레일 투 코브',
                sub_detail    = '잭퍼셀 트레일 투 코브',
                feature       = '잭퍼셀 트레일 투 코브',
                feature_image = 'image',
                is_main = True
            ),
            Detail(
                name          = '잭퍼셀 샤아니 레더',
                main_detail   = '잭퍼셀 샤아니 레더',
                sub_detail    = '잭퍼셀 샤아니 레더',
                feature       = '잭퍼셀 샤아니 레더',
                feature_image = 'image',
                is_main = True
            )
        ])

        ColorFilter.objects.bulk_create([
            ColorFilter( name = 'black'),
            ColorFilter( name = 'kahki'),
            ColorFilter( name = 'white')
        ])

        Color.objects.bulk_cerate([
            Color(color_category = ColorFilter.objects.get(id=1),name = '블랙'),
            Color(color_category = ColorFilter.objects.get(id=2),name = '노마드카키'),
            Color(color_category = ColorFilter.objects.get(id=3),name = '화이트'),
            Color(color_category = ColorFilter.objects.get(id=4),name = '페일퍼티')])

        TypeFilter.objects.create(name='스니커즈')
        
        GenderSegmentation.objects.create(name='남녀공용')

        Shoe.objects.bulk_create([
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(id = 1),
                detail              = Detail.objects.get(id = 1),
                gender_segmentation = GenderSegmentation.objects.get(id = 1),
                price               = 109000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(id = 1),
                detail              = Detail.objects.get(id = 2),
                gender_segmentation = GenderSegmentation.objects.get(id = 1),
                price               = 75000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(id = 1),
                detail              = Detail.objects.get(id = 2),
                gender_segmentation = GenderSegmentation.objects.get(id = 1),
                price               = 79000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(id = 1),
                detail              = Detail.objects.get(id = 3),
                gender_segmentation = GenderSegmentation.objects.get(id = 1),
                price               = 89000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(id = 1),
                detail              = Detail.objects.get(id = 4),
                gender_segmentation = GenderSegmentation.objects.get(id = 1),
                price               = 99000
            ),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(id = 1),
                detail              = Detail.objects.get(id = 5),
                gender_segmentation = GenderSegmentation.objects.get(id = 1),
                price               = 85000),
            Shoe(
                main_category       = MainCategory.objects.get(id = 1),
                shoe_category       = ShoeCategory.objects.get(id = 1),
                type_filter         = TypeFilter.objects.get(id = 1),
                detail              = Detail.objects.get(id = 6),
                gender_segmentation = GenderSegmentation.objects.get(id = 1),
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
                is_hover   = True
            ),
            SubImage(
                shoe_color = ShoeColor.objects.get(id = 2),
                image      = 'https://image.converse.co.kr/cmsstatic/product/560251C_560251C_03.jpg?browse=',
                is_hover   = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 3),
                image       ='https://image.converse.co.kr/cmsstatic/product/560250C_560250C_03.jpg?browse=',
                is_hover    = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 4),
                image       ='https://image.converse.co.kr/cmsstatic/product/27379/560846C_560846C_03.jpg?browse=',
                is_hover    = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 5),
                image       ='https://image.converse.co.kr/cmsstatic/product/168976C_168976C_03.jpg?browse=',
                is_hover    = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 6),
                image       ='https://image.converse.co.kr/cmsstatic/product/168695C_168695C_03.jpg?browse=',
                is_hover    = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 7),
                image       ='https://image.converse.co.kr/cmsstatic/product/168140C_168140C_03.jpg?browse=',
                is_hover    = True
            ),
            SubImage(
                shoe_color  = ShoeColor.objects.get(id = 8),
                image       ='https://image.converse.co.kr/cmsstatic/product/168135C_168135C_03.jpg?browse=',
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

        def test_mainpageview_success(self):
            client = Cliend()
            response = client.GET('/product/mainpage')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(),{
                "products": [
                    {
                        "page_one": [
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
                        ]
                    },
                    {
                        "page_two": [
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
                        ]
                    },
                    {
                        "page_three": [
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
                ]
            })

