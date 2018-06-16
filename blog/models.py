from django.db import models


class Article(models.Model):

    POSTED = 'POS'
    DRAFT = 'PEN'
    DELETED = 'DEL'
    STATUSES = (
        (POSTED, 'Publicado'),
        (DRAFT, 'Borrador'),
        (DELETED, 'Eliminado')
    )

    OTHER = 'OTH'
    TECH = 'TEC'
    INTERNET = 'NET'
    NEWS = 'NWS'
    LAGS = 'LAG'
    TAGS = (
        (OTHER, 'Otros'),
        (TECH, 'Tech'),
        (INTERNET, 'Internet'),
        (NEWS, 'Noticias'),
        (LAGS, 'Humor')
    )

    title = models.CharField(max_length=160)

    tags = models.CharField(max_length=3, choices=TAGS)
    created_on = models.DateTimeField(auto_now_add=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUSES, default=DRAFT)
    subtitle = models.TextField()
    content = models.TextField()
    blockquote = models.TextField(null=True, blank=True)
    image_l = models.FileField()
    image_m = models.FileField()
    image_s = models.FileField()
