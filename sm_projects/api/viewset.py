from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from sm_projects.models import Project
from .serializers import ProjectSerializer, ProjectAssignEmployeesSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @detail_route(['post', ])
    def assign(self, request, pk):
        serializer = ProjectAssignEmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True})
        else:
            return Response({"success": False})
