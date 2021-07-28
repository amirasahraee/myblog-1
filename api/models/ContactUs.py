from django.db import models


class ContactUs(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    message = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName)
