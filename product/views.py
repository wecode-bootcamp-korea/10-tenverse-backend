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

class DetailView(View):
    def get(self, request, product_id):
        try:
            shoe = ShoeColor.objects.filter(**{
                'id' : product_id
            })
            
            shoe_detail = list(shoe.values('id', 'shoe__detail__name', 'shoe__price', 'shoe__gender_segmentation__name', 'shoe__detail__main_detail','color__name', 'shoe__detail__sub_detail', 'shoe__detail__feature', 'shoe__detail__feature_image', 'image__image'))
            
            subimage_list = [image['subimage__image'] for image in shoe.values('subimage__image')]
            shoe_detail.append({'subimage_list' :subimage_list})

            shoe_color_list = list(ShoeColor.objects.filter(**{
                'shoe__id' : shoe[0].shoe.id
            }).values('id', 'image__image'))
            shoe_detail.append(shoe_color_list)
            
            size_list = [size['shoe__size__name'] for size in shoe.values('shoe__size__name')]
            shoe_detail.append({'size_list' : size_list})

            return JsonResponse({'product' : list(shoe_detail)}, status=200)
        except IndexError:
            return JsonResponse({'message' : 'NON_EXISTING_PRODUCT'})
