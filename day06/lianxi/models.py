from django.db import models

# Create your models here.

class Cartoon(models.Model):
    name = models.CharField(
        max_length=20
    )
    cover = models.FileField(
        verbose_name='封面',
        upload_to='cover',
    )
    class Meta:
        db_table = 'cartoon'