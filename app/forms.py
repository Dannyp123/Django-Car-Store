from django import forms

class PostVehicleForm(forms.Form):
    car_img = forms.URLField(
        widget=forms.TextInput(attrs={
            "class" : "form-control mb-3",
            "placeholder" : "Image URL"
        })
    )
