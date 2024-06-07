from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo3(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)

def _str_(self):
    return self.todo3_name
