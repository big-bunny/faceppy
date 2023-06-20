from django.db import models

class Face(models.Model):
    # Define fields for the Face model
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faces/')
    # Add any other fields you need for the Face model
    
    def __str__(self):
        return self.name
