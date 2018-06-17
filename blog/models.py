from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    thumb = models.FileField()
    status = models.BooleanField(default=True)

    def __str__(self):

        return '{0} - {1}'.format(self.created_on, self.title)
