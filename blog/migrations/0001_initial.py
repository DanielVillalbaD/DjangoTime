# Generated by Django 2.0.6 on 2018-06-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('tags', models.CharField(choices=[('OTH', 'Otros'), ('TEC', 'Tech'), ('NET', 'Internet'), ('NWS', 'Noticias'), ('LAG', 'Humor')], max_length=3)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('POS', 'Publicado'), ('PEN', 'Borrador'), ('DEL', 'Eliminado')], default='PEN', max_length=3)),
                ('subtitle', models.TextField()),
                ('content', models.TextField()),
                ('blockquote', models.TextField(blank=True, null=True)),
                ('image_l', models.FileField(upload_to='')),
                ('image_m', models.FileField(upload_to='')),
                ('image_s', models.FileField(upload_to='')),
            ],
        ),
    ]
