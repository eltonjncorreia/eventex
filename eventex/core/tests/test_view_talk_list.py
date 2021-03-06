from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.core.models import Talk, Speaker


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(title="Titulo da palestra",
                            start="10:00",
                            description="Descrição da Palestra")

        t2 = Talk.objects.create(title="Titulo da palestra",
                            start="13:00",
                            description="Descrição da Palestra")

        speaker = Speaker.objects.create(name='Henrique Bastos',
                                         slug='henrique-bastos',
                                         website='http://henriquebastos.net')

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)

        self.response = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Titulo da palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (2, '/palestrantes/henrique-bastos'),
            (2, 'Henrique'),
            (2, 'Descrição da Palestra')
        ]

        for count, expect in contents:
            with self.subTest():
                self.assertContains(self.response, expect, count)

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)

class TalkListGetEmpty(TestCase):
    def test_get_empy(self):
        response = self.client.get(r('talk_list'))

        self.assertContains(response, 'Ainda não existem palestras de manhã')
        self.assertContains(response, 'Ainda não existem palestras de tarde')