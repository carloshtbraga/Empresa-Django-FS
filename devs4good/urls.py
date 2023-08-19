from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("funcionarios/", views.funcionarios, name="funcionarios"),
    path('funcionario/<int:pk>/', views.funcionario_detail, name='funcionario_detail'),
    path("linguagens/", views.lista_linguagens, name="lista_linguagens"),
    path("novo_funcionario/", views.novo_funcionario, name="novo_funcionario"),
    path("cargos/", views.lista_cargos, name="lista_cargos"),
    path("novo_cargo/", views.novo_cargo, name="novo_cargo"),
    path("nova_linguagem/", views.nova_linguagem, name="nova_linguagem"),
    path("logout/", views.logout, name="logout"),
    path("funcionarios_filtro_salario/", views.funcionarios_filtro_salario, name="funcionarios_filtro_salario"),
    # Outras rotas do aplicativo devs4good podem ser definidas aqui
]
