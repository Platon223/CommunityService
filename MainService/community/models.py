from django.db import models

# Create your models here.

class Community(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    private = models.BooleanField()
    members = models.IntegerField()
    publish_date = models.DateField()

    def __str__(self):
        return self.id