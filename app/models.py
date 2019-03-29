from django.db import models


# Create your models here.
class VehiclePost(models.Model):
    car_img = models.URLField()
    year = models.IntegerField()
    make = models.TextField()
    model = models.TextField()
    mileage = models.IntegerField()

    # def __str__(self):
    #     return '''
    #     Car Image: {}
    #     Car Make: {}
    #     '''.format(self.car_img, self.make)

    @staticmethod
    def submit_vehicle_post(car_img, year, make, model, mileage):
        VehiclePost(
            car_img=car_img,
            year=year,
            make=make,
            model=model,
            mileage=mileage).save()
