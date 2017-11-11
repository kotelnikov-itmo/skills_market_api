from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from sm_projects.models import Project, Assignment
from sm_employees.models import Employee
from .serializers import ProjectSerializer, ProjectAssignEmployeesSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @detail_route(['post', ])
    def assign(self, request, pk):
        assignment_set = request.data['assignment_set']
        for a_data in assignment_set:
            try:
                assignment = Assignment.objects.get(id=a_data["id"])
            except Assignment.DoesNotExist:
                return Response({"success": False, "error": "Assignment Does Not Exist"})
            else:
                assignment.employee = Employee.objects.get(id=a_data["employee"])
                assignment.save()
        return Response({"success": True, "error": ""})
        # else:
        #     return Response({"success": False, "error": "Invalid Data"})
