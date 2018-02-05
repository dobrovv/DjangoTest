from rest_framework import generics, mixins

from . import models
from . import serializers

from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict

import json

# Return the list of users in the database
class UserView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        users_vals =  models.User.objects.all().values(
            'id', 'username', 'date_joined', 'is_active'
        )
        
        return JsonResponse(list(users_vals), safe=False)

# Return the currently logged in user
class UserMeView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            return JsonResponse(model_to_dict(user))
        else:
            return JsonResponse({'error': 'User is not logged in'})

# Register a new user and log him in
class UserRegisterView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # expected Content-Type: application/json
        # expected Json Body: {'username':'myname', password:'mypassword'}
        try:
            raw_data = json.loads(request.body)
            username = raw_data.get('username')
            password = raw_data.get('password')

            models.User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return JsonResponse(model_to_dict(user))

        except BaseException as e: #either a json, key or model validation error
            print(repr(e))
            return JsonResponse({'error': repr(e)}, status=400)

#Log the user in
class UserLoginView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # expected Content-Type: application/json
        # expected Json Body: {'username':'myname', password:'mypassword'}
        try:
            raw_data = json.loads(request.body)
            username = raw_data.get('username')
            password = raw_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse(model_to_dict(user))
            else:
                return JsonResponse({'error': 'Wrong username/password'})


        except BaseException as e: #either a json or key error
            print(str(e))
            return JsonResponse({'error': repr(e)}, status=400)


# Log the user out
class UserLogoutView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'status':'done'})
        else:
            return JsonResponse({'error': 'User is not logged in'})
