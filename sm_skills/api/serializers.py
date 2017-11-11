from rest_framework.serializers import ModelSerializer

from sm_skills.models import Skill


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', ]