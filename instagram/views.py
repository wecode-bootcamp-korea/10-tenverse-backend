from django.views import View
from django.http  import JsonResponse

from .models import Instagram

class InstagramView(View):
    def get(self, request):
        page = int(request.GET.get('page', 0))
        limit = int(request.GET.get('limit',20))
        posts = Instagram.objects.all().values()[page*limit:((page+1)*limit)]
        return JsonResponse({'posts' : list(posts)}, status=200)

