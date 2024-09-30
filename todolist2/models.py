from django.db import models
from django.contrib.auth.models import User

# Data model for a todo-list item
class Item(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    ip_addr = models.GenericIPAddressField()

    def __str__(self):
        return f'id={self.id}, text="{self.text}"'
