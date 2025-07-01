from rest_framework import generics
from core.models import LearningMaterial
from core.serializers import LearningMaterialSerializer

class LearningMaterialListView(generics.ListAPIView):
    queryset = LearningMaterial.objects.all()
    serializer_class = LearningMaterialSerializer
