from django.shortcuts import render
from django.views import View
from app import forms
from app import models

# Create your views here.


class LandingPage(View):
    def get(self, request):
        return render(request, "home.html")


class MenuPage(View):
    def get(self, request):
        return render(request, "menu.html")