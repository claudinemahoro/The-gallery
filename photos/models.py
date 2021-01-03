from django.db import models

# Create your models here.

import datetime as dt

class Photographer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    def __str__(self):
        return self.first_name
    def save_photographer(self):
        self.save()
    def delete_photographer(self):
        self.delete()
    @classmethod
    def display_photographers(cls):
        photographers=Photographer.objects.all()
        for photographer in photographers:
            return photographer
    class Meta:
        ordering=['first_name']

class Location(models.Model):
    photo_location=models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def update_location(self,update):
        self.photo_location=update
        self.save()
    @classmethod
    def get_location_id(cls,id):
        locate=Location.objects.get(pk=id)
        return locate
    
    def __str__(self):
        return self.photo_location