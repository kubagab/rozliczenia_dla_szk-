from rest_framework import serializers
from .models import Students, Grade, Parents, Operators, Payments, Transfer


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operators
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'
