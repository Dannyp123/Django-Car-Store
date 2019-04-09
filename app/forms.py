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

STATES = (
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR' ,'OR'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY')
)


class PostVehicleForm(forms.Form):
    car_img = forms.URLField(
        widget=forms.TextInput(attrs={
            "class": "input-feild black-text"
        }))
    year = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "input-feild",
        }))
    make = forms.CharField(
        widget=forms.Select(
            choices=CHOICES, attrs={"class": "input-feild"}))

    model = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input-feild"
        }))
    price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "input-feild"
        }))
    mileage = forms.IntegerField(
        widget=forms.TextInput(attrs={
            "class": "input-feild"
        }))
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "materialize-textarea"
        }))

class BuyingCarForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild"
        })
    )
    street = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild",
        })
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild"
        })
    )
    state = forms.CharField(
        widget=forms.Select(
            choices=STATES, attrs={"class": "form-control mb-3"}))

    z_code = forms.CharField(
        widget=forms.TextInput(attrs={
            "class" : "input-feild"
        })
    )
    p_number = forms.RegexField(
         regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
          widget=forms.TextInput(attrs={
            "class" : "input-feild"
        })   
    )