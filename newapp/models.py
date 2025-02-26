from django.db import models
# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    country = models.CharField(max_length= 150)
    def __str__(self):
        return f"{self.firstname} {self.lastname} from {self.country}"

#We can Write More ...
    