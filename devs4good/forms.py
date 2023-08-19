from django import forms
from .models import Cargo, LinguagemProgramacao, Funcionario, InformacoesFuncionario


class FuncionarioForm(forms.ModelForm):
    linguagens = forms.ModelMultipleChoiceField(
        queryset=LinguagemProgramacao.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Funcionario
        fields = ["nome", "cargo", "linguagens"]


class InformacoesFuncionarioForm(forms.ModelForm):
    class Meta:
        model = InformacoesFuncionario
        fields = ["cidade", "estado", "idade", "frase_preferida", "pokemon_preferido"]


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ["nome", "salario"]


class LinguagensForm(forms.ModelForm):
    class Meta:
        model = LinguagemProgramacao
        fields = ["nome"]
