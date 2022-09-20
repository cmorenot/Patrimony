# Generated by Django 2.0.2 on 2018-05-29 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rol', '0001_initial'),
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateField(auto_now=True)),
                ('historical_meaning', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de significado hisorico-----')),
                ('historical_singularity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de singularidad historica')),
                ('historical_representativeness', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de representatividad historica')),
                ('social_meaning', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de significado social-----')),
                ('social_singularity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de singularidad social')),
                ('social_representativeness', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de representatividad social')),
                ('natural_meaning', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de significado natural-----')),
                ('natural_singularity_space', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor espacial de singularidad natural')),
                ('natural_singularity_storm', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor temporal de singularidad natural')),
                ('natural_representativeness_space', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor espacial e representatividad natural')),
                ('natural_representativeness_storm', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor temporal de representatividad natural')),
                ('natural_integrity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de integridad natural')),
                ('integrity_it_interns_quantitative', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de integridad interna cuantitativa')),
                ('integrity_it_interns_qualitative', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de integridad interna cualitativa')),
                ('social_utility', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de utilidad social')),
                ('economic_utility', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Valor de utilidad economica')),
                ('qualitative_evaluation', models.TextField(blank=True, null=True, verbose_name='Evalucion cualitativa')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('objective', models.CharField(max_length=200)),
                ('responsible', models.CharField(max_length=100)),
                ('start_up', models.DateField(verbose_name='Tiempo de creado')),
                ('start_end', models.DateField(verbose_name='Tiempo de acabado')),
                ('finish', models.BooleanField(default=False, verbose_name='Terminado')),
                ('authors', models.ManyToManyField(to='rol.Profile', verbose_name='Autores')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.Resource', verbose_name='Recurso')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_new', models.IntegerField(blank=True, null=True, verbose_name='Nueva categoria')),
                ('time_is_over', models.DateField(verbose_name='Hasta cuando')),
                ('destroy', models.BooleanField(default=True, verbose_name='Acabar tiempo')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='Proyecto Trasladado')),
                ('user_giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rol.Profile', verbose_name='Dador')),
                ('user_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Receptor')),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='Proyecto'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.Resource', verbose_name='Recurso'),
        ),
    ]