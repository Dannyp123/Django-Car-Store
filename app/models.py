from django.db import models


# Create your models here.
class VehiclePost(models.Model):
    car_img = models.URLField()
    year = models.IntegerField()
    make = models.TextField()
    model = models.TextField()
    mileage = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=100)

    # def __str__(self):
    #     return '''
    #     Car Image: {}
    #     Car Make: {}
    #     '''.format(self.car_img, self.make)

    @staticmethod
    def submit_vehicle_post(car_img, year, make, model, mileage, price,
                            description):
        VehiclePost(
            car_img=car_img,
            year=year,
            make=make,
            model=model,
            mileage=mileage,
            price=price,
            description=description).save()


class BuyVehicle(models.Model):
    name = models.TextField()

    @staticmethod
    def submit_vehicle_purchase(name):
        BuyVehicle(name=name)
