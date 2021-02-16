from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.TextField(blank=False, null=False)
    type = models.IntegerField(max_length=1, blank=False, null=False)
