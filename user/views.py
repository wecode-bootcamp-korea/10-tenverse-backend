import json
import jwt
import bcrypt
import re

from django.views import View
from django.http  import JsonResponse

from converse.settings import SECRET_KEY
from my_settings       import ALGORITHM
from .models           import (
    User,
    Gender,
)

def validation(email, password):
    if len(password) < 8:
        return False
    email_lambdas = [
        lambda x : '@' in x,
        lambda x : '.' in x
    ]
    password_lambdas = [
        lambda x : x in ['!', '@', '#', '$', '%', '&', '*'],
        lambda x : x in ['0','1','2','3','4','5','6','7','8','9']
    ]
    for lambdas in email_lambdas:
        if not lambdas(email):
            return False
    for lambdas in password_lambdas:
        if not any(lambdas(i) for i in password):
            return False
    return True

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validation(data['email'], data['password']):
                return JsonResponse({'message' : 'VALIDATION_ERROR'}, status=401)
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'EXISTING_ACCOUNT'}, status=400)
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            User(
                name         = data['name'],
                phone_number = data['phone_number'],
                birth_date   = data['birth_date'],
                gender_id    = Gender.objects.get(name = data['gender']).id,
                email        = data['email'],
                password     = hashed_password.decode('utf-8'),
            ).save()
            return JsonResponse({'message' : 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validation(data['email'], data['password']):
                return JsonResponse({'message' : 'VALIDATION_ERROR'}, status=401)
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token =  jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)
                    return JsonResponse({'access_token' : access_token.decode('utf-8')}, status = 200)
                return JsonResponse({'message' : 'UNAUTHORIZED'}, status = 401)
            return JsonResponse({'message' : 'UNAUTHORIZED'}, status = 401)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
