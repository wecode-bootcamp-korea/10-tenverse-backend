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

class MainPageView(View):
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
        page = int(request.GET.get('page', 0))
        limit = int(request.GET.get('limit', 20))
        filters = {
            'gender_filters'    : [gender.name for gender in GenderSegmentation.objects.all()],
            'color_filters'     : [color.name for color in ColorFilter.objects.all()],
            'type_filters'      : [typefilter.name for typefilter in TypeFilter.objects.all()],
            'size_filters'      : [size.name for size in Size.objects.all()]
        }

        shoes = ShoeColor.objects.filter(subimage__is_hovered = True).annotate(
            name       = F('shoe__detail__name'),
            price      = F('shoe__price'),
            main_image = F('image__image'),
            sub_image  = F('subimage__image')
        ).values('id','shoe__id', 'name', 'price', 'main_image', 'sub_image')[page*limit:((page+1)*limit)-1]
        
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
        return JsonResponse({'filters' : filters, 'products' : shoe_list}, status=200)

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
            ).exclude(
                id = product.values().first()['id']
            ).annotate(
                main_image = F('image__image')
            ).values('id', 'main_image'))

            color_list.insert(0, {
                'id'         : shoe_detail[0]['id'],
                'main_image' : shoe_detail[0]['main_image']
            })

            size_list = [size['shoecolorsize__size__name'] for size in product.values('shoecolorsize__size__name')]
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

class FilterView(View):
    def get(self, request):
        page = int(request.GET.get('page', 0))
        limit = int(request.GET.get('limit', 20))
        colorfilter  = request.GET.getlist('color', list(ColorFilter.objects.all().values_list('name', flat=True)))
        typefilter   = request.GET.getlist('type', list(TypeFilter.objects.all().values_list('name', flat=True)))
        genderfilter = request.GET.getlist('gender', list(GenderSegmentation.objects.all().values_list('name', flat=True)))
        sizefilter   = request.GET.getlist('size', list(Size.objects.all().values_list('name', flat=True)))
        
        shoes = ShoeColor.objects.filter(**{
            'color__color_category__name__in'     : colorfilter,
            'shoe__type_filter__name__in'         : typefilter,
            'shoe__gender_segmentation__name__in' : genderfilter,
            'shoecolorsize__size__name__in'       : sizefilter,
            'subimage__is_hovered'                : True
        }).distinct()
        
        shoe_values = list(shoes.annotate(
            name       = F('shoe__detail__name'),
            price      = F('shoe__price'),
            main_image = F('image__image'),
            sub_image  = F('subimage__image')
        ).values('id','shoe__id', 'name', 'price', 'main_image', 'sub_image')[page*limit:((page+1)*limit)-1])

        filters = {
            'gender_filters'    : list(shoes.values_list('shoe__gender_segmentation__name',flat=True)),
            'color_filters'     : [color.name for color in ColorFilter.objects.all()],
            'type_filters'      : list(shoes.values_list('shoe__type_filter__name',flat=True)),
            'size_filters'      : list(shoes.values_list('shoecolorsize__size__name',flat=True))
        }

        shoe_list = [{'product_detail' : shoe} for shoe in shoe_values]
        
        for shoe in shoe_list:
            shoe['color_list'] = list(Color.objects.filter(**{
                'shoecolor__shoe__id'             : shoe['product_detail']['shoe__id'],
                'shoecolor__subimage__is_hovered' : True
            }).annotate(
                shoe_id      = F('shoecolor__id'),
                color_filter = F('color_category__name'),
                main_image   = F('shoecolor__image__image'),
                sub_image    = F('shoecolor__subimage__image')
            ).values('shoe_id', 'color_filter', 'main_image', 'sub_image'))
        return JsonResponse({'filters' : filters, 'products' : shoe_list}, status=200)

