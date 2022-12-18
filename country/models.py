from django.db import models
from django.contrib.auth import get_user_model

class Country(models.Model):
    country_name = models.CharField(max_length=255)
    worldcup_count = models.IntegerField()
    latest_worldcup_year = models.IntegerField()
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, editable=True)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = "countries"
