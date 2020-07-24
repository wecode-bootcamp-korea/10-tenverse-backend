import time

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
        filter_list = [{
            'gender_filters' : [gender.name for gender in GenderSegmentation.objects.all()],
            'color_filters'  : [color.name for color in ColorFilter.objects.all()],
            'type-filters'   : [typefilter.name for typefilter in TypeFilter.objects.all()],
            'size_filters'   : [size.name for size in Size.objects.all()]
        }]
        return JsonResponse({'filters' : filter_list}, status=200)

class ShoesView(View):
    def get(self, request):
        shoe_list   = []
        shoes       = Shoe.objects.all().prefetch_related('color').select_related('detail').
        for shoe in shoes:
            name             = Detail.objects.get(id = shoe.detail_id).name
            price            = shoe.price
            colorfilter_list = []
            shoecolors       = ShoeColor.objects.filter(shoe_id = shoe.id).select_related('image').prefetch_related('subimage_set')
            
            for colors in shoecolors:
                image        = colors.image.image
                sub_image    = SubImage.objects.filter(shoe_color = colors).first().image
                colorfilters = Color.objects.select_related('color_category').filter(id = colors.color_id)

                for color in colorfilters:
                    colorfilter_list.append({
                        'id'    : color.id,
                        'color' : ColorFilter.objects.get(id=color.color_category.id).name
                    })
                
                shoe_list.append({
                    'name'        : name,
                    'price'       : price,
                    'imgUrl'      : image,
                    'hoverImgUrl' : sub_image,
                    'colors'      : colorfilter_list
                })
                
            for shoe in shoe_list:
                if shoe['name'] == name:
                    shoe['colors'] = colorfilter_list
        return JsonResponse({'products' : shoe_list}, status=200)
