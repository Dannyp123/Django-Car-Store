from django import forms

CHOICES = (
    ('Acura', 'Acura'),
    ('Audi', 'Audi'),
    ('Bentley', 'Bentley'),
    ('BMW', 'BMW'),
    ('Bugatti', 'Bugatti'),
    ('Buick', 'Buick'),
    ('Cadillac', 'Cadillac'),
    ('Chevy', 'Chevy'),
    ('Chrystler', 'Chrystler'),
    ('Dodge', 'Dodge'),
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Ford', 'Ford'),
    ('GMC', 'GMC'),
    ('Honda', 'Honda'),
    ('Hyundai', 'Hyundai'),
    ('Infiniti', 'Infiniti'),
    ('Jaguar', 'Jaguar'),
    ('Jeep', 'Jeep'),
    ('Lamboghini', 'Lamboghini'),
    ('Land Rover', 'Land Rover'),
    ('Lexus', 'Lexus'),
    ('Maserati', 'Maserati'),
    ('Mazda', 'Mazda'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Nissan', 'Nissan'),
    ('Porsche', 'Porsche'),
    ('Rolls Royce', 'Rolls Royce'),
    ('Toyota', 'Toyota'),
    ('Volkswagen', 'Volkswagen'),
    ('Volvo', 'Volvo')
)


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
    price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control mb-3",
            "placeholder": "$ Price"
        }))
    mileage = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "form-control mb-3",
            "placeholder": "Cars Mileage"
        }))
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control mb-3",
            "placeholder": "Short description"
        }))