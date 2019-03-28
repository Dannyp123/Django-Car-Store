from django.db import models


# Create your models here.
class VehiclePost(models.Model):
    car_img = models.URLField()
    make = models.TextField()

    # def __str__(self):
    #     return '''
    #     Car Image: {}
    #     Car Make: {}
    #     '''.format(self.car_img, self.make)

    @staticmethod
    def submit_vehicle_post(car_img, make):
        VehiclePost(car_img=car_img, make=make).save()
