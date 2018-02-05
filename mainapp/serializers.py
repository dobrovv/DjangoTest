from rest_framework import serializers
from . import models

from django.contrib.auth.validators import UnicodeUsernameValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'id', 'username', 'password'
        )
        extra_kwargs = {
            'username': {
                #'validators': [UnicodeUsernameValidator()],
            }
        }
