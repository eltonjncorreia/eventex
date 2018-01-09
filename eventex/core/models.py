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
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    kINDS =(
        (EMAIL, 'Email'),
        (PHONE, 'Telefone')
    )
    speaker = models.ForeignKey('Speaker', verbose_name='palestrante')
    kind = models.CharField(max_length=1, choices=kINDS)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.value