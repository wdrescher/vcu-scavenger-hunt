from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from vcuhunt.landmarks.models import Landmark

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    completed_landmark = models.ManyToManyField(Landmark)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_completion(self): 
        completed = self.completed_landmark.all().count()
        total = Landmark.objects.all().count()
        return round((completed / total) * 100)
