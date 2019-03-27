from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render (request, "landing.html")

class PostVehicle(View):
    def get(self, request):
        return render (request, "post-vehicle.html", {"post_form" : forms.PostVehicleForm()})

    def post(self, request):

