from django.core.exceptions import ValidationError
from django.test import TestCase
from pip._vendor.distro import name

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link.hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net'
        )

        self.assertTrue(contact.objects.exists())


    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-99999999'
        )

        self.assertTrue(contact.objects.exists())


    def test_choices(self):
        """Contact Kind shoude be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind='E',
            value='henrique@bastos.net'
        )
        self.assertEqual('henrique@bastos.net', str(contact))


class ContactManageTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos',
                                   slug='henrique-bastos',
                                   photo='http://hbn.link/hb-pic')

        s.contact_set.create(kind=Contact.EMAIL, value='henrique@bastos.net')
        s.contact_set.create(kind=Contact.PHONE, value='21-99999999')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['henrique@bastos.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected =['21-99999999']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
















