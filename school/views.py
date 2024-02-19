from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



from .models import Students, Grade, Parents, Operators, Payments, Transfer
from .serializers import StudentsSerializer, GradeSerializer, ParentsSerializer, OperatorSerializer, PaymentsSerializer, \
    TransferSerializer


# @authentication_classes([JWTAuthentication])
class StudentsListView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def finalize_response(self, request, response, *args, **kwargs):
        # Call the parent class's finalize_response method
        response = super().finalize_response(request, response, *args, **kwargs)

        # Add your custom headers here
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'

        return response


class ParentsByStudentView(ListAPIView):
    serializer_class = ParentsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Students, id=student_id)
        parents = Parents.objects.filter(children=student)
        return parents



class GradeListView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GradeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class ParentsListView(generics.ListCreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ParentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class OperatorListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = OperatorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class OperatorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = OperatorSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PaymentsListView(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TransferListView(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TransferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]