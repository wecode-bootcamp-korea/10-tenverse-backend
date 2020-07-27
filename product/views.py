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
    ShoeSize,
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
                'shoecolor__shoe__id'           : shoe_list[i]['product_detail']['shoe__id'],
                'shoecolor__subimage__is_hovered' : True
            }).annotate(
                    shoe_id      = F('shoecolor__id'),
                    color_filter = F('color_category__name'),
                    main_image   = F('shoecolor__image__image'),
                    sub_image    = F('shoecolor__subimage__image')
                ).values('shoe_id', 'color_filter', 'main_image', 'sub_image'))
        return JsonResponse({'products' : shoe_list}, status=200)

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
                shoe__id = product.values('shoe__id').first()['shoe__id']
            ).annotate(
                main_image = F('image__image')
            ).values('id', 'main_image'))

            size_list = [size['shoe__size__name'] for size in product.values('shoe__size__name')]
            shoe_detail.append({
                'sub_image'  : sub_image,
                'color_list' : color_list,
                'size_list'  : size_list
            })
            return JsonResponse({'product' : shoe_detail}, status=200)
        except IndexError:
            return JsonResponse({'message' : 'NON_EXISTING_PRODUCT'}, status=400)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
