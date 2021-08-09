from django.db import models
class contactus(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    queries = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name