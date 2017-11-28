from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class subscriptionFormTest(TestCase):
    def test_form_has_field(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expect = ['name','cpf','email','phone']
        self.assertSequenceEqual(expect, list(form.fields))


    def test_cpf_is_digit(self):
        form = self.make_validated_form(cpf='ABDC23455')
        self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas numeros')


    def test_cpf_has_11(self):
        form = self.make_validated_form(cpf='12345')
        self.assertFormErrorCode(form, 'cpf', 'length')


    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        execption = errors_list[0]
        self.assertEqual(code, execption.code)


    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)


    def make_validated_form(self, **kwargs):
        valid = dict(name="Henrique Bastos", cpf='12345',
                    phone="21212121", email='henrique@bastos.net')

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form





