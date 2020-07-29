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
    ShoeColorSize,
    MainImage,
    ShoeColor,
    SubImage
)

'''class MainPageView(View):
    def get(self, request):
        shoe = ShoeColor.objects.filter(**{
            'shoe__detail__is_main' : True,
            'subimage__is_hovered'  : True
        }).annotate(
            name       = F('shoe__detail__name'),
            price      = F('shoe__price'),
            main_image = F('image__image'),
            sub_image  = F('subimage__image')
        ).values('id','name', 'price','main_image','sub_image')
        
        shoes = {
            'women_collection' : list(shoe.filter(shoe__detail__name__contains = '척테일러')),
            'jack_purcell'      : list(shoe.filter(color__name = '노마드카키')),
            'pro_leather'       : list(shoe.filter(**{
                'shoe__detail__name__contains' : '잭퍼셀',
                'color__name'                  : '화이트'
            }))
        }

        return JsonResponse({'products' : shoes}, status=200)

class ShoesView(View):
    def get(self, request):
        page = request.GET.get('page', None)
        
        shoes = ShoeColor.objects.filter(subimage__is_hovered = True).annotate(
            name       = F('shoe__detail__name'),
            price      = F('shoe__price'),
            main_image = F('image__image'),
            sub_image  = F('subimage__image')
        ).values(
            'id','shoe__id', 'name', 'price', 'main_image', 'sub_image'
        )[int(page)*20:((int(page)+1)*20)-1]

        shoe_list = [{'product_detail' : shoe} for shoe in shoes]
        
        for shoe in shoe_list:
            shoe['color_list'] = list(Color.objects.filter(**{
                'shoecolor__shoe__id'               : shoe['product_detail']['shoe__id'],
                'shoecolor__subimage__is_hovered'   : True
            }).annotate(
                    shoe_id      = F('shoecolor__id'),
                    color_filter = F('color_category__name'),
                    main_image   = F('shoecolor__image__image'),
                    sub_image    = F('shoecolor__subimage__image')
            ).values('shoe_id', 'color_filter', 'main_image', 'sub_image'))
        
        return JsonResponse({'products' : shoe_list}, status=200)
'''
class ShoeCategoryView(View):
    def get(self, request, category_name):
        page = int(request.GET.get('page', 0))
        limit = int(request.GET.get('limit', 20))
        filters = {
            'genders' : [gender['name'] for gender in GenderSegmentation.objects.filter(shoe__shoe_category__name = category_name).values('name').distinct()],
            'colors'  : [color['name'] for color in ColorFilter.objects.filter(color__shoe__shoe_category__name = category_name).values('name').distinct()],
            'types'   : [type_filter['name'] for type_filter in TypeFilter.objects.filter(shoe__shoe_category__name = category_name).values('name').distinct()],
            'sizes'   : [size['name'] for size in Size.objects.filter(shoecolorsize__shoecolor__shoe__shoe_category__name = category_name).values('name').distinct()]
        }
        
        shoes = ShoeColor.objects.filter(
            subimage__is_hovered = True,
            shoe__shoe_category__name = category_name
        ).prefetch_related(
            "shoe",
            "shoe__detail",
            "image",
            'subimage_set'
        )[page*limit:((page+1)*limit)-1]

        shoe_list = [{
            'product_detail' : {
                "id"         : shoe.id,
                "shoe__id"   : shoe.shoe.id,
                "name"       : shoe.shoe.detail.name,
                "price"      : int(shoe.shoe.price),
                "main_image" : shoe.image.image,
                "sub_image"  : shoe.subimage_set.get(is_hovered=True).image
            }} for shoe in shoes]
        
        for shoe in shoe_list:
            shoe['product_detail']['color_list'] = [{
                'shoe_id'      : color.shoecolor_set.filter(shoe=shoe['product_detail']['shoe__id']).first().id,
                "color_filter" : color.color_category.name,
                "main_image"   : color.shoecolor_set.filter(shoe=shoe['product_detail']['shoe__id']).first().image.image,
                "sub_image"    : color.shoecolor_set.filter(shoe=shoe['product_detail']['shoe__id']).first().subimage_set.get(is_hovered=True).image
            } for color in Color.objects.filter(
                shoecolor__shoe__id             = shoe['product_detail']['shoe__id'],
                shoecolor__subimage__is_hovered = True
            ).prefetch_related(
                'shoecolor_set',
                'color_category',
                'shoecolor_set__image',
                'shoecolor_set__subimage_set'
            )]
        
        return JsonResponse({'filters' : filters, 'products' : shoe_list}, status=200)
