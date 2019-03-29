from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render(request, "landing.html",
                      {"car_post": models.VehiclePost.objects.all()})


class PostVehicle(View):
    def get(self, request):
        return render(request, "post-vehicle.html",
                      {"post_form": forms.PostVehicleForm()})

    def post(self, request):
        form = forms.PostVehicleForm(data=request.POST)
        if form.is_valid():
            car_img = form.cleaned_data["car_img"]
            year = form.cleaned_data["year"]
            make = form.cleaned_data["make"]
            model = form.cleaned_data["model"]
            mileage = form.cleaned_data["mileage"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]



            models.VehiclePost.submit_vehicle_post(car_img, year, make, model,
                                                   mileage, price, description)
            return redirect("landing")
        else:
            return render(request, "post-vehicle.html", {"post_form": form})


class VehicleSale(View):
    def get(self, request, id):
        return render(request, "car-page.html",
                      {"car_post": models.VehiclePost.objects.get(id=id)})
