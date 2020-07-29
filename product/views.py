from django.views     import View
from django.http      import JsonResponse

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
        shoes = ShoeColor.objects.filter(
            shoe__detail__is_main = True,
            subimage__is_hovered = True
        ).prefetch_related(
            "shoe__detail",
            "image",
            "subimage_set"
        )
        shoe_list = {
            'women_collection' : [{
                "id"         : shoe.id,
                "name"       : shoe.shoe.detail.name,
                "price"      : int(shoe.shoe.price),
                "main_image" : shoe.image.image,
                "sub_image"  : shoe.subimage_set.get(is_hovered=True).image
            } for shoe in shoes.filter(shoe__detail__name__contains = '척테일러')],
            'jack_purcell' : [{
                "id"         : shoe.id,
                "name"       : shoe.shoe.detail.name,
                "price"      : int(shoe.shoe.price),
                "main_image" : shoe.image.image,
                "sub_image"  : shoe.subimage_set.get(is_hovered=True).image
            } for shoe in shoes.filter(color__name = '노마드카키')],
            'pro_leather' : [{
                'id'         : shoe.id,
                'name'       : shoe.shoe.detail.name,
                'price'      : int(shoe.shoe.price),
                'main_image' : shoe.image.image,
                'sub_image'  : shoe.subimage_set.get(is_hovered=True).image
            } for shoe in shoes.filter(
                shoe__detail__name__contains = '잭퍼셀',
                color__name = '화이트'
            )]
        }
        return JsonResponse({'products' : shoe_list}, status=200)

class ShoesView(View):
    def get(self, request):
        page = int(request.GET.get('page', 0))
        limit = int(request.GET.get('limit', 20))
        
        filters = {
            'gender_filters' : [gender.name for gender in GenderSegmentation.objects.all()],
            'color_filters'  : [color.name for color in ColorFilter.objects.all()],
            'type_filters'   : [typefilter.name for typefilter in TypeFilter.objects.all()],
            'size_filters'   : [size.name for size in Size.objects.all()]
        }

        shoes = ShoeColor.objects.filter().prefetch_related(
            "shoe",
            "image",
            "subimage_set",
            "shoe__detail"
        )[page*limit:((page+1)*limit)-1]
        
        shoe_list = [{
            "product_detail" : {
                "id"         : shoe.id,
                "name"       : shoe.shoe.detail.name,
                "price"      : int(shoe.shoe.price),
                "main_image" : shoe.image.image,
                "sub_image"  : shoe.subimage_set.get(is_hovered=True).image,
                "color_list" : [{
                    "shoe_id"      : color.shoecolor_set.filter(shoe__id=shoe.shoe.id).first().id,
                    "color_filter" : color.color_category.name,
                    "main_image"   : color.shoecolor_set.filter(shoe__id=shoe.shoe.id).first().image.image,
                    "sub_image"    : color.shoecolor_set.filter(shoe__id=shoe.shoe.id).first().subimage_set.get(is_hovered=True).image
                } for color in Color.objects.filter(
                    shoecolor__shoe__id = shoe.shoe.id,
                ).prefetch_related(
                    "shoecolor_set",
                    "color_category",
                    "shoecolor_set__image",
                    "shoecolor_set__subimage_set"
                )]
            }
        } for shoe in shoes]
        
        return JsonResponse({'filters' : filters, 'products' : shoe_list}, status=200)

class DetailView(View):
    def get(self, request, product_id):
        try:
            product = ShoeColor.objects.filter(id = product_id).prefetch_related(
                "shoe",
                "shoe__gender_segmentation",
                "shoe__detail",
                "color",
                "image",
                "subimage_set",
                "size"
            ).first()

            color_list = [{
                'id'         : shoe.id,
                "main_image" : shoe.image.image
            } for shoe in ShoeColor.objects.filter(
                shoe = product.shoe
            ).prefetch_related(
                "image"
            ).exclude(
                id = product.id
            )]

            color_list.insert(0, {
                'id'         : product.id,
                'main_image' : product.image.image
            })

            shoe_detail = {
                "id"            : product.id,
                "name"          : product.shoe.detail.name,
                "price"         : int(product.shoe.price),
                "gender"        : product.shoe.gender_segmentation.name,
                "color_name"    : product.color.name,
                "main_detail"   : product.shoe.detail.main_detail,
                "sub_detail"    : product.shoe.detail.sub_detail,
                "features"      : product.shoe.detail.feature,
                "feature_image" : product.shoe.detail.feature_image,
                "main_image"    : product.image.image,
                "sub_image"     : [image.image for image in product.subimage_set.all()],
                "size_list"     : [size.name for size in product.size.all()],
                "color_list"    : color_list
            } 

            return JsonResponse({'product' : shoe_detail}, status=200)
        except IndexError:
            return JsonResponse({'message' : 'NON_EXISTING_PRODUCT'}, status=400)
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
