from django.db import models

# Create your models here.
class Landmark(models.Model): 
    name = models.CharField(blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("landmarks:detail", kwargs={"id": self.id})
