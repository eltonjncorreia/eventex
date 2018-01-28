from django.db import models
from django.shortcuts import resolve_url as r


# Create your models here.
from eventex.core.managers import EmailContactManager, PhoneContactManager


class Speaker(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug')
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

    object = models.Manager()
    emails = EmailContactManager()
    phones = PhoneContactManager()


    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.value


class Talk(models.Model):
    title = models.CharField('titulo', max_length=200)
    start = models.TimeField('inicio', blank=True, null=True)
    description = models.TextField('descricao', blank=True)
    speakers = models.ManyToManyField('Speaker', blank=True, verbose_name='palestrantes')

    class Meta:
        verbose_name = 'Talk'
        verbose_name_plural = 'Talks'

    def __str__(self):
        return self.title
