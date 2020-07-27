from django.views import View
from django.http  import JsonResponse

from .models import Instagram

class InstagramView(View):
    def get(self, request):
        posts = Instagram.objects.all().values()
        return JsonResponse({'posts' : list(posts)}, status=200)

