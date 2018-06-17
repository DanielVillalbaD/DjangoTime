from django.db import models

class Tag(models.Model):
    name= models.CharField(max_length=16)

    def __str__(self):

        return '{0}'.format(self.name)
