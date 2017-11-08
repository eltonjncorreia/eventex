from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class subscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_field(self):
        """Form must have 4 fields"""
        expect = ['name','cpf','email','phone']
        self.assertSequenceEqual(expect, list(self.form.fields))

