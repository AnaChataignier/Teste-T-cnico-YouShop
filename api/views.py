from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import PlantedTree
from .serializers import PlantedTreeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class PlantedTreeListAPIView(generics.ListAPIView):
    serializer_class = PlantedTreeSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PlantedTree.objects.filter(user=user)
