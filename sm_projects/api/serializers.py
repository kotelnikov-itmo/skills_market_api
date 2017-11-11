from rest_framework.serializers import ModelSerializer, StringRelatedField

from sm_projects.models import Project, Assignment
from sm_skills.models import Skill
from sm_skills.api.serializers import SkillSerializer
from sm_employees.models import Position
from sm_employees.api.serrializers import PositionSerializer


class AssignmentSerializer(ModelSerializer):
    need_skills = SkillSerializer(many=True)
    position = PositionSerializer()

    class Meta:
        model = Assignment
        fields = [
            'employee', 'description', 'position', 'need_skills', 'id'
        ]


class ProjectSerializer(ModelSerializer):
    assignment_set = AssignmentSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'start_date', 'assignment_set', 'end_date'
        ]

    def create(self, validated_data):
        assignments = validated_data.pop('assignment_set')
        project = Project(**validated_data)
        project.save()
        for a in assignments:
            a["project_id"] = project.id
            a["position"], _ = Position.objects.get_or_create(name=a["position"]["name"])
            _skills = []
            for skill_data in a.pop("need_skills"):
                _skill, _ = Skill.objects.get_or_create(name=skill_data['name'])
                _skills.append(_skill)
            assignment = Assignment(**a)
            print(assignment)
            assignment.save()
            assignment.need_skills = _skills
            assignment.save()
        return project


class AssignmentEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'employee']


class ProjectAssignEmployeesSerializer(ModelSerializer):
    assignment_set = AssignmentEmployeeSerializer(many=True)

    class Meta:
        model = Project
        fields = ['assignment_set', ]