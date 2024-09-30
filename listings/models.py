from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    num_of_bedrooms = models.IntegerField()
    num_of_bathrooms = models.IntegerField()
    size_of_property = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.title