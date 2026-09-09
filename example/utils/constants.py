from django.db import models

class Provider(models.TextChoices):
    OTHER = "other", "Other"