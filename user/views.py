import json
import jwt
import bcrypt
import re

from django.views       import View
from django.http        import JsonResponse
from django.db.models   import Q

from converse.settings import SECRET_KEY
from my_settings       import ALGORITHM
from .models           import (
    User,
    Gender,
)

def email_validation(email):
    lambdas = [
        lambda x : '@' in x,
        lambda x : '.' in x
    ]
    for lam in lambdas:
        if not lam(email):
            return False
    return True

def password_validation(password):
    if len(password) < 8:
        return False
    lambdas = [
        lambda x : x in ['!', '@', '#', '$', '%', '&', '*'],
        lambda x : x in [str(i) for i in range(10)]
    ]
    for lam in lambdas:
        if not any(lam(i) for i in password):
            return False
    return True

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not(email_validation(data['email']) or password_validation(data['password'])):
                return JsonResponse({'message' : 'VALIDATION_ERROR'}, status=401)
            if User.objects.filter(Q(email=data['email']) | Q(phone_number=data['phone_number'])).exists():
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
            if not email_validation(data['email']):
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
