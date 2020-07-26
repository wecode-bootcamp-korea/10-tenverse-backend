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

class DetailView(View):
    def get(self, request, product_id):
        try:
            product = ShoeColor.objects.filter(id = product_id)
            
            shoe_detail = list(product.annotate(
                name          = F('shoe__detail__name'),
                price         = F('shoe__price'),
                gender        = F('shoe__gender_segmentation__name'),
                color_name    = F('color__name'),
                main_detail   = F('shoe__detail__main_detail'),
                sub_detail    = F('shoe__detail__sub_detail'),
                features      = F('shoe__detail__feature'),
                feature_image = F('shoe__detail__feature_image'),
                main_image    = F('image__image')
            ).values(
                'id', 'name', 'price', 'gender', 'color_name', 'main_detail', 'sub_detail', 'features', 'feature_image', 'main_image'
            ))
            sub_image = [image['subimage__image'] for image in product.values('subimage__image')]
            
            color_list = list(ShoeColor.objects.filter(
                shoe__id = list(product.values('shoe__id'))[0]['shoe__id']
            ).annotate(
                main_image = F('image__image')
            ).values('id', 'main_image'))
            size_list = [size['shoe__size__name'] for size in product.values('shoe__size__name')]
            shoe_detail.append({'options' : {
                'sub_image'  : sub_image,
                'color_list' : color_list,
                'size_list'  : size_list
            }})
            return JsonResponse({'product' : shoe_detail }, status=200)
        except IndexError:
            return JsonResponse({'message' : 'NON_EXISTING_PRODUCT'})
