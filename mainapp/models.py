from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#https://stackoverflow.com/questions/44109/extending-the-user-model-with-custom-fields-in-django
#https://docs.djangoproject.com/en/2.0/topics/db/examples/one_to_one/
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
