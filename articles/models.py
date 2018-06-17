from django.contrib.auth.models import User
from django.db import models

from blog.models import Blog
from tags.models import Tag


class Article(models.Model):
    POSTED = 'POS'
    DRAFT = 'PEN'
    DELETED = 'DEL'
    STATUSES = (
        (POSTED, 'Publicado'),
        (DRAFT, 'Borrador'),
        (DELETED, 'Eliminado')
    )

    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.SET(1))
    tags = models.ManyToManyField(
        Tag,
        through='Article',
        through_fields=('Otros', 'Tech', 'Internet', 'Noticias', 'Humor'),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUSES, default=POSTED)
    subtitle = models.TextField()
    content = models.TextField()
    image_l = models.FileField()
    image_m = models.FileField()
    image_s = models.FileField()
    thumb = models.FileField()
    loves = models.IntegerField(null=True, default=0)
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)

    def __str__(self):
        return '{0} - {1}'.format(self.created_on, self.title)
