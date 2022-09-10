from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict

from .serializers import WomenSerializer
from .models import Women

# Create your views here.
class WomenAPIView(APIView):  # APIView - все API наследуются от него
    def get(self, request):  # обработка get запроса
        lst = Women.objects.all().values()
        return Response({"posts": list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"],
        )
        return Response({"post": model_to_dict(post_new)})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
k = {"title": "Ekaterina", "content": "Ekaterina Malysheva", "cat_id": 2}
