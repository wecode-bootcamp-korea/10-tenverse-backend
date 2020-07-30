from django.views import View
from django.http  import JsonResponse

from .models import Instagram

class InstagramView(View):
    def get(self, request):
        page = int(request.GET.get('page',0))
        limit = int(request.GET.get('limit',0))
        posts = list(Instagram.objects.all().values())[page*limit:(page+1)*limit]
        return JsonResponse({'posts' : posts}, status=200)

