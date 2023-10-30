from django.shortcuts import render
from rest_framework import generics
from .models import Students, Grade, Parents, Operators, Payments, Transfer
from .serializers import StudentsSerializer, GradeSerializer, ParentsSerializer, OperatorSerializer, PaymentsSerializer, \
    TransferSerializer


class StudentsListView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    lookup_field = 'id'


class GradeListView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class GradeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'id'


class ParentsListView(generics.ListCreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer


class ParentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
    lookup_field = 'id'


class OperatorListView(generics.ListCreateAPIView):
    queryset = Operators.objects.all()
    serializer_class = OperatorSerializer


class OperatorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operators.objects.all()
    serializer_class = OperatorSerializer
    lookup_field = 'id'


class PaymentsListView(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    lookup_field = 'id'


class TransferListView(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class TransferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    lookup_field = 'id'