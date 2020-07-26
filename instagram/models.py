from django.db import models

class Instagram(models.Model):
    user               = models.CharField(max_length = 50)
    user_profile_image = models.CharField(max_length = 300)
    image              = models.CharField(max_length = 300)
    text               = models.CharField(max_length = 300)

    class Meta:
        db_table = 'instagram'
