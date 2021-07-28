from django.db import models


class Post(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=250)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.createAt)
