from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render(request, "landing.html")


class PostVehicle(View):
    def get(self, request):
        return render(request, "post-vehicle.html",
                      {"post_form": forms.PostVehicleForm()})

    def post(self, request):
        form = forms.PostVehicleForm(data=request.POST)
        if form.is_valid():
            car_img = form.cleaned_data["car_img"]
            models.VehiclePost.submit_vehicle_post(car_img)
            return redirect("post-vehicle")
        else:
            return render(request, "post-vehicle.html", {"post_form": form})


class PostedVehicle(View):
    def get(self, request):
        return render(request, "posted-vehicles.html",
                      {"car_post": models.VehiclePost.objects.all()})
