from django.db import models
from django.shortcuts import resolve_url as r

# Create your models here.
class Speaker(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('SLug')
    website = models.URLField('Website',blank=True)
    photo = models.URLField("Photo")
    description = models.TextField("Descrição", blank=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural ='Palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)