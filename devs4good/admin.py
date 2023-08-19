from django.contrib import admin
from .models import Cargo, Funcionario, InformacoesFuncionario, LinguagemProgramacao

admin.site.register(Cargo)
admin.site.register(Funcionario)
admin.site.register(InformacoesFuncionario)
admin.site.register(LinguagemProgramacao)
