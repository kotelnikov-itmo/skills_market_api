from rest_framework.serializers import ModelSerializer, CharField

from sm_skills.models import Skill


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ['name', ]
        extra_kwargs = {
            'name': {'validators': []},
        }