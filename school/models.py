from django.contrib.auth.models import User
from django.db import models


class Parents(models.Model):
    first_name = models.CharField(max_length=16, null=False)
    last_name = models.CharField(max_length=32, null=False)
    children = models.ManyToManyField('Students')
    phone = models.CharField(max_length=9, null=False)
    email = models.EmailField(max_length=32, null=False)
    date_joined = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)


class Grades(models.Model):
    name = models.CharField(max_length=9)


class Students(models.Model):
    first_name = models.CharField(max_length=16, null=False)
    last_name = models.CharField(max_length=32, null=False)
    grade = models.ForeignKey('Grades', on_delete=models.CASCADE)


class Transfer(models.Model):
    title = models.CharField(max_length=64, null=False)
    amount = models.IntegerField(null=False)
    parent = models.ForeignKey('Parents', on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(null=False)


class Payments(models.Model):
    title = models.CharField(max_length=64)
    period_start = models.DateTimeField(null=False)
    period_end = models.DateTimeField(null=False)
    parent = models.ForeignKey(Parents, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    priority = models.IntegerField(null=False)


# class Operators(models.Model):
#     first_name = models.CharField(max_length=16)
#     last_name = models.CharField(max_length=32)
#     email = models.EmailField(null=False)
#     password = models.CharField(max_length=64, null=False)
#     date_joined = models.DateTimeField(null=False)
#     modified_at = models.DateTimeField(null=False)
#     last_login = models.DateTimeField(null=False)


class Operators(models.Model):
    operator = models.OneToOneField(User, on_delete=models.CASCADE)
