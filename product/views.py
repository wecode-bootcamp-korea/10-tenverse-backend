from django.views   import View
from django.http    import JsonResponse

class ShoesView(View):
    def get(self, request):
        return JsonResponse({'message' : 'test'}, status=200)
