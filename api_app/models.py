from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TrialModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    creator = models.ForeignKey(
        User, related_name="trial_models", on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
