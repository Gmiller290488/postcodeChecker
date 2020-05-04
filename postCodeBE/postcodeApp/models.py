from django.conf import settings
from django.db import models

class User(models.Model):
    email = models.TextField()
    postcode = models.TextField()

    def getEmailForPostCode(self):
        return self.postcode

    def __str__(self):
        return self.email