from django.views   import View
from django.http    import JsonResponse

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
        shoe_list   = []
        shoes       = Shoe.objects.prefetch_related('shoecolor_set').select_related('detail').all()
        for shoe in shoes:
            name             = shoe.detail.name
            price            = shoe.price
            colorfilter_list = []
            shoecolors       = shoe.shoecolor_set.prefetch_related('image').prefetch_related('subimage_set').filter(shoe=shoe.id)
            
            for colors in shoecolors:
                image        = colors.image.image
                sub_image    = colors.subimage_set.get(is_hover=1).image
                colorfilters = shoe.color.select_related('color_category').filter(id = colors.color_id)

                for color in colorfilters:
                    colorfilter_list.append({
                        'id'    : color.id,
                        'color' : color.color_category.name
                    })
                
                shoe_list.append({
                    'name'        : name,
                    'price'       : price,
                    'image'       : image,
                    'hover_image' : sub_image,
                    'colors'      : colorfilter_list
                })
                
            for shoe in shoe_list:
                if shoe['name'] == name:
                    shoe['colors'] = colorfilter_list
        return JsonResponse({'products' : shoe_list}, status=200)
