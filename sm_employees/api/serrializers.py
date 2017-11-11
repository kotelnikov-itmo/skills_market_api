from rest_framework.serializers import ModelSerializer, StringRelatedField

from sm_employees.models import Employee


class EmployeeSerializer(ModelSerializer):
    skills = StringRelatedField(many=True)

    class Meta:
        model = Employee
        fields = [
            'name', 'surname', 'middlename', 'recruited_date', 'skills'
        ]