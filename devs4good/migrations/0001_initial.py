# Generated by Django 4.2.4 on 2023-08-19 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cargo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("salario", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "cargo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="devs4good.cargo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LinguagemProgramacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="InformacoesFuncionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cidade", models.CharField(max_length=50)),
                ("estado", models.CharField(max_length=2)),
                ("idade", models.IntegerField()),
                ("frase_preferida", models.TextField()),
                ("pokemon_preferido", models.CharField(max_length=20)),
                (
                    "funcionario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="devs4good.funcionario",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="funcionario",
            name="linguagens",
            field=models.ManyToManyField(to="devs4good.linguagemprogramacao"),
        ),
    ]
