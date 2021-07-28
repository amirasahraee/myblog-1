from django.db import models


class Meta(models.Model):
    key = models.CharField(max_length=250, unique=True)
    value = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images',null=True,blank=True)

    def __str__(self):
        return self.key
