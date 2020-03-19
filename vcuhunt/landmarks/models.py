from django.db import models
from django.urls import reverse

# Create your models here.
class Landmark(models.Model): 
    name = models.CharField(blank=True, max_length=255)
    image_url = models.CharField(blank=True, max_length=500)
    address = models.CharField(blank=True, max_length=500)
    description = models.CharField(blank=True, max_length=500)
    question = models.CharField(blank=True, max_length=500)
    c_answer = models.CharField(blank=True, max_length=500)
    answer1 = models.CharField(blank=True, max_length=500)
    answer2 = models.CharField(blank=True, max_length=500)
    answer3 = models.CharField(blank=True, max_length=500)
    answer4 = models.CharField(blank=True, max_length=500)
    map_query = models.CharField(blank=True, max_length=500)

    def get_absolute_url(self):
        return reverse("landmarks:detail", kwargs={"id": self.id})
    
    def __str__(self): 
        return self.name; 
