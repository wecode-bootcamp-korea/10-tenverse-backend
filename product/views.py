from django.views   import View
from django.http    import JsonResponse

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
        shoes = list(ShoeColor.objects.filter(**{
            'shoe__detail__is_main' : 'True',
            'color__name__in' : ['화이트', '노마드카키'],
            'subimage__is_hover' : 'True'
        }).values('id', 'color_id__name','shoe_id__price','image__image', 'subimage__image'))
        shoes.append(list(ShoeColor.objects.filter(**{
            'shoe_id__detail__name' : '척테일러 올스타 리프트 캔버스',
            'color_id__name' : '블랙',
            'subimage__is_hover' : 'True'
        }).values('id', 'color_id__name','shoe_id__price','image__image', 'subimage__image'))[0])
        return JsonResponse({'product' : shoes}, status=200)

