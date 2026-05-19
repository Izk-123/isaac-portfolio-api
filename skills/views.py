from rest_framework.generics import ListAPIView
from .models import SkillCategory
from .serializers import SkillCategorySerializer

class SkillListView(ListAPIView):
    queryset = SkillCategory.objects.all().prefetch_related('skills')
    serializer_class = SkillCategorySerializer