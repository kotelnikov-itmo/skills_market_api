from rest_framework.viewsets import ModelViewSet


from sm_skills.models import Skill
from .serializers import SkillSerializer


class SkillsViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', False)
        if query:
            return Skill.objects.filter(name__istartswith=query)
        else:
            return Skill.objects.all()

