from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="语言名字"
    )
    desc = models.CharField(
        max_length=100,
        verbose_name="描述"
    )
    def get_desc(self):
        return "爱的你理由:%s" % self.desc