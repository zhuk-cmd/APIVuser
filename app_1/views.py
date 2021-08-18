from rest_framework.response import  Response
from rest_framework.decorators import api_view
from app_1.models import Employee
from app_1.serializer import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet


class APIVall_data(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@api_view(['GET'])
def api_user(request, pk):
    if request.method == 'GET':
        users = Employee.objects.filter(parent=pk)
        serializer = EmployeeSerializer(users, many=True)
        return Response(serializer.data)


