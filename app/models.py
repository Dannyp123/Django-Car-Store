from django.db import models

# Create your models here.
class VehiclePost(models.Model):
    car_img = models.URLField()


    def __str__(self):
        return '''
        Car Image: {}
        '''.format(self.car_img)
    
    @staticmethod
    def submit_vehicle_post(car_img):
        VehiclePost(car_img=car_img).save()
