from django.views     import View
from django.http      import JsonResponse
from django.db.models import F

from .models import (
    MainCategory,
    ShoeCategory,
    Shoe,
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

class CategoryView(View):
    def get(self, request):
        filter_list = {
            'gender_filters' : [gender.name for gender in GenderSegmentation.objects.all()],
            'color_filters'  : [color.name for color in ColorFilter.objects.all()],
            'type_filters'   : [typefilter.name for typefilter in TypeFilter.objects.all()],
            'size_filters'   : [size.name for size in Size.objects.all()]
        }
        return JsonResponse({'filters' : filter_list}, status=200)

class MainPageView(View):
    def get(self, request):
        shoes = {}
        shoe = ShoeColor.objects.filter(**{
            'shoe__detail__is_main' : True,
            'subimage__is_hovered'  : True
        }).annotate(
            name       = F('shoe__detail__name'),
            price      = F('shoe__price'),
            main_image = F('image__image'),
            sub_image  = F('subimage__image')
        ).values('id','name','price','main_image','sub_image')
        
        shoes['womens_collection'] = list(shoe.filter(shoe__detail__name__contains = '척테일러'))
        
        shoes['jack_purcell'] = list(shoe.filter(color__name = '노마드카키'))
        
        shoes['pro_leather'] = list(shoe.filter(**{
            'shoe__detail__name__contains' : '잭퍼셀',
            'color__name'                  : '화이트'
        }))

        return JsonResponse({'products' : shoes}, status=200)

class ShoesView(View):
    def get(self, request):
        shoes = ShoeColor.objects.filter(subimage__is_hovered = True).annotate(
            name       = F('shoe__detail__name'),
            price      = F('shoe__price'),
            main_image = F('image__image'),
            sub_image  = F('subimage__image')
        ).values('id','shoe__id', 'name', 'price', 'main_image', 'sub_image')
        
        shoe_list = [{'product_detail' : shoe} for shoe in shoes]
        
        for i in range(0,len(shoe_list)):
            shoe_list[i]['color_list'] = list(Color.objects.filter(**{
                'shoecolor__shoe__id'               : shoe_list[i]['product_detail']['shoe__id'],
                'shoecolor__subimage__is_hovered'   : True
            }).annotate(
                    shoe_id      = F('shoecolor__id'),
                    color_filter = F('color_category__name'),
                    main_image   = F('shoecolor__image__image'),
                    sub_image    = F('shoecolor__subimage__image')
                ).values('shoe_id', 'color_filter', 'main_image', 'sub_image'))
        
        return JsonResponse({'products' : shoe_list}, status=200)
