# from django.test import TestCase, Client
# from django.urls import reverse
# from .models import Funcionario, Cargo, LinguagemProgramacao


# class TestUrls(TestCase):
#     def setUp(self):
#         self.client = Client()

#         cargo = Cargo.objects.create(nome="Desenvolvedor", salario=5000)
#         linguagem_python = LinguagemProgramacao.objects.create(nome="Python")
#         linguagem_java = LinguagemProgramacao.objects.create(nome="Java")

#         self.funcionario = Funcionario.objects.create(
#             nome="Funcionario Teste", cargo=cargo
#         )
#         self.funcionario.linguagens.set([linguagem_python, linguagem_java])

#     def test_funcionario_detail_url(self):
#         response = self.client.get(
#             reverse("funcionario_detail", args=[self.funcionario.pk])
#         )
#         self.assertEqual(response.status_code, 200)

#     def test_index_url(self):
#         response = self.client.get(reverse("index"))
#         self.assertEqual(response.status_code, 200)

#     def test_funcionarios_url(self):
#         response = self.client.get(reverse("funcionarios"))
#         self.assertEqual(response.status_code, 200)

#     def test_lista_linguagens_url(self):
#         response = self.client.get(reverse("lista_linguagens"))
#         self.assertEqual(response.status_code, 200)

#     def test_novo_funcionario_url(self):
#         response = self.client.get(reverse("novo_funcionario"))
#         self.assertEqual(response.status_code, 200)
