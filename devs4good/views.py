from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Funcionario, LinguagemProgramacao, Cargo
from .forms import (
    FuncionarioForm,
    InformacoesFuncionarioForm,
    CargoForm,
    LinguagensForm,
)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def index(request):
    return render(request, "devs4good/index.html")


def inicio(request):
    return render(
        request, "devs4good/inicio.html", {"messages": messages.get_messages(request)}
    )


@login_required
def funcionarios(request):
    funcionarios = Funcionario.objects.all().order_by("pk")
    return render(
        request, "devs4good/funcionarios.html", {"funcionarios": funcionarios}
    )


@login_required
def funcionario_detail(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(
        request, "devs4good/funcionario_detail.html", {"funcionario": funcionario}
    )


@login_required
def lista_linguagens(request):
    linguagens = LinguagemProgramacao.objects.all()
    return render(
        request, "devs4good/lista_linguagens.html", {"linguagens": linguagens}
    )


@login_required
def nova_linguagem(request):
    if request.method == "POST":
        form_linguagem = LinguagensForm(request.POST)

        if form_linguagem.is_valid():
            form_linguagem.save()
            return redirect("index")
    else:
        form_linguagem = LinguagensForm()

    return render(
        request,
        "devs4good/nova_linguagem.html",
        {
            "form_linguagem": form_linguagem,
        },
    )


@login_required
def novo_funcionario(request):
    if request.method == "POST":
        form_funcionario = FuncionarioForm(request.POST)
        form_informacoes = InformacoesFuncionarioForm(request.POST)
        if form_funcionario.is_valid() and form_informacoes.is_valid():
            funcionario = form_funcionario.save()
            informacoes = form_informacoes.save(commit=False)
            informacoes.funcionario = funcionario
            informacoes.save()
            return redirect("index")
    else:
        form_funcionario = FuncionarioForm()
        form_informacoes = InformacoesFuncionarioForm()

    return render(
        request,
        "devs4good/novo_funcionario.html",
        {
            "form_funcionario": form_funcionario,
            "form_informacoes": form_informacoes,
        },
    )


@login_required
def lista_cargos(request):
    cargos = Cargo.objects.all()
    print("weeeeeeeeeeeeeeeeee", cargos)
    return render(request, "devs4good/lista_cargos.html", {"cargos": cargos})


@login_required
def novo_cargo(request):
    if request.method == "POST":
        form_cargo = CargoForm(request.POST)

        if form_cargo.is_valid():
            form_cargo.save()
            return redirect("index")
    else:
        form_cargo = CargoForm()

    return render(
        request,
        "devs4good/novo_cargo.html",
        {
            "form_cargo": form_cargo,
        },
    )


def cadastro(request):
    if request.method == "GET":
        return render(request, "devs4good/cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        userExists = User.objects.filter(username=username).first()
        emailExists = User.objects.filter(email=email).first()

        if userExists:
            return HttpResponse("Usuário com esse nome já existe")
        if emailExists:
            return HttpResponse("Email já cadastrado")

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()

        return redirect("index")


def login(request):
    if request.method == "GET":
        return render(request, "devs4good/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        validUser = authenticate(username=username, password=password)

        if validUser is not None:
            auth_login(request, validUser)
            return redirect("index")
        else:
            return HttpResponse("Usuário ou senha inválidos")


def logout(request):
    auth_logout(request)
    messages.success(request, "Você foi deslogado com sucesso.")
    return redirect("inicio")


def funcionarios_filtro_salario(request):
    valor_minimo = request.GET.get("minimo")
    valor_maximo = request.GET.get("maximo")

    funcionarios = Funcionario.objects.all()

    if valor_minimo:
        funcionarios = funcionarios.filter(cargo__salario__gte=valor_minimo)

    if valor_maximo:
        funcionarios = funcionarios.filter(cargo__salario__lte=valor_maximo)

    return render(
        request,
        "devs4good/funcionarios_filtro_salario.html",
        {"funcionarios": funcionarios},
    )
