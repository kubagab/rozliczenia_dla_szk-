from django.contrib import admin
from django.urls import path, re_path, include
from .views import StudentsListView, StudentDetailView, GradeListView, GradeDetailView, ParentsListView, \
    ParentDetailView, OperatorListView, OperatorDetailView, PaymentsListView, PaymentDetailView, TransferListView, \
    TransferDetailView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('students/', StudentsListView.as_view(), name='student_list'),
    path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail'),
    path('grades/', GradeListView.as_view(), name='grades_list'),
    path('grade/<int:id>/', GradeDetailView.as_view(), name='grade_detail'),
    path('parents/', ParentsListView.as_view(), name='parents_list'),
    path('parent/<int:id>/', ParentDetailView.as_view(), name='parent_view'),
    path('operators/', OperatorListView.as_view(), name='operator_list'),
    path('operator/<int:id>/', OperatorDetailView.as_view(), name='operator_detail'),
    path('payments/', PaymentsListView.as_view(), name='payments_list'),
    path('payment/<int:id>', PaymentDetailView.as_view(), name='payment_detail'),
    path('transfers/', TransferListView.as_view(), name='transfer_list'),
    path('transfer/<int:id>/', TransferDetailView.as_view(), name='transfer_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
