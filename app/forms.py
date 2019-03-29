from django import forms

CHOICES = (('Ford', 'Ford'), ('Chevy', 'Chevy'))


class PostVehicleForm(forms.Form):
    car_img = forms.URLField(
        widget=forms.TextInput(attrs={
            "class": "form-control mb-3",
            "placeholder": "Image URL"
        }))
    year = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control mb-3",
            "placeholder": "Cars Year"
        }))
    make = forms.CharField(
        widget=forms.Select(
            choices=CHOICES, attrs={"class": "form-control mb-3"}))

    model = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control mb-3",
            "placeholder": "Cars Model"
        }))
    mileage = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control mb-3",
            "placeholder": "Cars Mileage"
        }))