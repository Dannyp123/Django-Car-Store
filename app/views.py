from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render (request, "landing.html")