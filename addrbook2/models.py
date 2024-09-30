from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    last_name     = models.CharField(max_length=20)
    first_name    = models.CharField(max_length=20)
    birthday      = models.DateField(blank=True, null=True)
    children      = models.IntegerField(blank=True, null=True)
    address       = models.CharField(blank=True, max_length=200)
    city          = models.CharField(blank=True, max_length=30)
    state         = models.CharField(blank=True, max_length=20)
    zip_code      = models.CharField(blank=True, max_length=10)
    country       = models.CharField(blank=True, max_length=30)
    email         = models.CharField(blank=True, max_length=32)
    phone_number  = models.CharField(blank=True, max_length=16)
    created_by    = models.ForeignKey(User, on_delete=models.PROTECT, related_name="entry_creators")
    creation_time = models.DateTimeField()
    updated_by    = models.ForeignKey(User, on_delete=models.PROTECT, related_name="entry_updators")
    update_time   = models.DateTimeField()

    def __str__(self):
        return f"Entry(id={self.id})"
