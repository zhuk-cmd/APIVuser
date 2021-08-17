from rest_framework import serializers
from app_1.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'position','date','inform', 'earnings','parent')