from django.db import models
from django.utils import timezone

class Seminar(models.Model):
    presenter=models.CharField(max_length=100)
    date=models.DateTimeField('Seminar Date')
    title=models.CharField('Title',max_length=1000)
    abstract=models.CharField('Abstract',max_length=10000,blank=True)
    bio=models.CharField('Biography',max_length=10000,blank=True)
    headshot=models.ImageField('Headshot',upload_to='headshots/',blank=True)

    def __str__(self):
        return self.presenter

    def is_past(self):
        return self.date<timezone.now()
