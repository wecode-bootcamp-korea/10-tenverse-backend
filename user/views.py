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
    UserDetail,
    Gender,
)

class SignUpView(View):
    def post(self, request):

        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message' : 'EXISTING_ACCOUNT'}, status = 400)
            if re.search(re.compile("[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"), data['email']):
                if re.search(re.compile("^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%&*])[a-zA-Z\d!@#$%&*]{8,}$"), data['password']):
                    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
                    UserDetail(
                        name         = data['name'],
                        phone_number = data['phone_number'],
                        birth_date   = data['birth_date'],
                        gender_id    = Gender.objects.get(name = data['gender']).id
                    ).save()
                    User(
                        email       = data['email'],
                        password    = hashed_password.decode('utf-8'),
                        user_detail = UserDetail.objects.get(name = data['name'], phone_number = data['phone_number'])
                    ).save()
                    return JsonResponse({'message' : 'SUCCESS'}, status = 200)
            return JsonResponse({'message' : 'VALIDATION_ERROR'}, status=401)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                   access_token =  jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)
                   return JsonResponse({'access_token' : access_token.decode('utf-8')}, status = 200)
            return JsonResponse({'message' : 'UNAUTHORIZED'}, status = 401)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
