from django.db import models

class moviedata(models.Model):
    moviename = models.CharField(max_length =100)
    movierating = models.CharField(max_length=10)
    movieyear = models.CharField(max_length = 5)
    movieimage = models.CharField(max_length=5000)
