from django.shortcuts import render
from django.views import View


# Create your views here.
class Register(View):
    def post(self, request):
