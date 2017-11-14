from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """ GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contains input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

        # maneira de se fazer acima, mas não é tao boa quanto

        # self.assertContains(self.response, '<form')
        # self.assertContains(self.response, '<input', 6)
        # self.assertContains(self.response, 'type="text"', 3)
        # self.assertContains(self.response, 'type="email"')
        # self.assertContains(self.response, 'type="submit"')


    def test_csrf(self):
        """Html must contains csrf """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    
class SubsribePostValid(TestCase):
    def setUp(self):
        """ verify POST should """
        data = dict(name="Henrique Bastos", phone="12345678901",
                    email="henrique@bastos.net", cpf="12345678901")
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())

class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        """invalid POST should in POST"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name="Henrique Bastos", cpf='12345678901',
                    email='henrique@bastos.net', phone='211212')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, "Inscricao realizada com sucesso")
