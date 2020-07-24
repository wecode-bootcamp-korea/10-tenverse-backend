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
        start_time = time.time()
        shoes = ShoeColor.objects.filter(**{
            'subimage__is_hover' : 'True'
        }).values('id','shoe__id','shoe__detail__name', 'shoe__price', 'image__image', 'subimage__image')
        shoe_list = [[shoe] for shoe in shoes]
        for i in range(len(shoe_list)):
            shoe_list[i].append(list(Color.objects.filter(**{
                'shoecolor__shoe__id' : shoe_list[i][0]['shoe__id']
            }).values('shoecolor__id', 'color_category__name')))
        return JsonResponse({'products' : shoe_list}, status=200)
