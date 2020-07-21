from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'genders'

class UserDetail(models.Model):
    name         = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 50, unique=True)
    birth_date   = models.DateField()
    gender       = models.ForeignKey(Gender, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_details'

class User(models.Model):
    email       = models.EmailField(max_length = 255, unique=True)
    password    = models.CharField(max_length = 100)
    user_detail = models.OneToOneField(UserDetail, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'users'

