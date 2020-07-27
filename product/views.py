from django.views     import View
from django.http      import JsonResponse
from django.db.models import F

from .models import (
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

class ShoesView(View):
    def get(self, request):
        return JsonResponse({'message' : 'test'}, status=200)

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

