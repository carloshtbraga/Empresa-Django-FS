from django.test import TestCase, Client
from django.urls import reverse


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_url(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_funcionarios_url(self):
        response = self.client.get(reverse("funcionarios"))
        self.assertEqual(response.status_code, 200)

    def test_funcionario_detail_url(self):
        # Suponha que você tenha um funcionário com id=1 no banco de dados
        response = self.client.get(reverse("funcionario_detail", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_lista_linguagens_url(self):
        response = self.client.get(reverse("lista_linguagens"))
        self.assertEqual(response.status_code, 200)

    def test_novo_funcionario_url(self):
        response = self.client.get(reverse("novo_funcionario"))
        self.assertEqual(response.status_code, 200)
