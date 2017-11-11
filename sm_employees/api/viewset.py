from rest_framework.viewsets import ReadOnlyModelViewSet

from sm_employees.models import Employee
from .serrializers import EmployeeSerializer


class EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = Employee.objects.filter(is_active=False)
    serializer_class = EmployeeSerializer
