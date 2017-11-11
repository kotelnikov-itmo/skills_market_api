from rest_framework.serializers import ModelSerializer, StringRelatedField

from sm_projects.models import Project, Assignment


class AssignmentSerializer(ModelSerializer):
    need_skills = StringRelatedField(many=True)
    position = StringRelatedField()

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
            'name', 'description', 'start_date', 'assignment_set'
        ]

class AssignmentEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'employee']


class ProjectAssignEmployeesSerializer(ModelSerializer):
    assignment_set = AssignmentEmployeeSerializer(many=True)

    class Meta:
        model = Project
        fields = ['assignment_set', ]