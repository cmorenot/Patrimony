from django.db import models
from apps.rol.models import Profile
from django.contrib.auth.models import User
from apps.resource.models import Resource
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
import math
# Create your models here.


class Project(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    authors = models.ManyToManyField(Profile, verbose_name='Autores')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, verbose_name='Recurso')
    objective = models.CharField(max_length=200)
    responsible = models.CharField(max_length=100)
    start_up = models.DateField(verbose_name='Tiempo de creado')
    start_end = models.DateField(verbose_name='Tiempo de acabado')
    finish = models.BooleanField(default=False, verbose_name='Terminado')

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return '{}'.format(self.name)


class Evaluation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, verbose_name='Recurso')
    time_create = models.DateField(auto_now=True)

    historical_meaning = models.PositiveSmallIntegerField(verbose_name='Valor de significado hisorico-----',  null=True, blank=True)
    historical_singularity = models.PositiveSmallIntegerField(verbose_name='Valor de singularidad historica',  null=True, blank=True)
    historical_representativeness = models.PositiveSmallIntegerField(verbose_name='Valor de representatividad historica',  null=True, blank=True)

    social_meaning = models.PositiveSmallIntegerField(verbose_name='Valor de significado social-----',  null=True, blank=True)
    social_singularity = models.PositiveSmallIntegerField(verbose_name='Valor de singularidad social',  null=True, blank=True)
    social_representativeness = models.PositiveSmallIntegerField(verbose_name='Valor de representatividad social',  null=True, blank=True)

    natural_meaning = models.PositiveSmallIntegerField(verbose_name='Valor de significado natural-----',  null=True, blank=True)
    natural_singularity_space = models.PositiveSmallIntegerField(verbose_name='Valor espacial de singularidad natural',  null=True, blank=True)
    natural_singularity_storm = models.PositiveSmallIntegerField(verbose_name='Valor temporal de singularidad natural', null=True, blank=True)
    natural_representativeness_space = models.PositiveSmallIntegerField(verbose_name='Valor espacial e representatividad natural',  null=True, blank=True)
    natural_representativeness_storm = models.PositiveSmallIntegerField(verbose_name='Valor temporal de representatividad natural',  null=True, blank=True)
    natural_integrity = models.PositiveSmallIntegerField(verbose_name='Valor de integridad natural',  null=True, blank=True)

    integrity_it_interns_quantitative = models.PositiveSmallIntegerField(verbose_name='Valor de integridad interna cuantitativa',  null=True, blank=True)
    integrity_it_interns_qualitative = models.PositiveSmallIntegerField(verbose_name='Valor de integridad interna cualitativa',  null=True, blank=True)

    social_utility = models.PositiveSmallIntegerField(verbose_name='Valor de utilidad social',  null=True, blank=True)
    economic_utility = models.PositiveSmallIntegerField(verbose_name='Valor de utilidad economica',  null=True, blank=True)

    qualitative_evaluation = models.TextField(verbose_name='Evalucion cualitativa', null=True, blank=True)

    def average_meaning(self):
        average = 0
        if self.social_meaning and self.natural_meaning and self.historical_meaning:
            average = (self.historical_meaning + self.natural_meaning + self.social_meaning)/3
        else:
            pass
        return average

    def average_singularity(self):
        average = 0
        if self.historical_singularity and self.social_singularity and self.natural_singularity_space and self.natural_singularity_storm:
            temp = (self.historical_singularity + self.social_singularity + self.natural_singularity_space +self.natural_singularity_storm)/4
            average = round(temp, 0)
        else:
            pass
        return average

    def average_representativeness(self):
        average = 0
        if self.historical_representativeness and self.social_representativeness and self.natural_representativeness_space and self.natural_representativeness_storm:
            temp = (self.historical_representativeness + self.social_representativeness + self.natural_representativeness_space + self.natural_representativeness_storm)/4
            average = round(temp, 0)
        return average

    def average_integrity(self):
        average = 0
        if self.natural_integrity and self.integrity_it_interns_quantitative and self.integrity_it_interns_qualitative:
            temp = (self.natural_integrity + self.integrity_it_interns_qualitative + self.integrity_it_interns_quantitative)/3
            average = round(temp, 0)
        else:
            pass
        return average

    def average_utility(self):
        average = 0
        if self.economic_utility and self.social_utility:
            temp = (self.economic_utility+self.social_utility)/2
            average = round(temp, 0)
        else:
            pass
        return average

    def authenticity(self):
        average = 0
        if self.average_meaning() and self.average_singularity() and self.average_representativeness() and self.average_integrity() and self.social_utility:
            temp = (self.average_meaning() + self.average_singularity() + self.average_representativeness() + self.average_integrity() + self.social_utility)/5
            average = round(temp, 0)
        else:
            pass
        return average

    def validate_ic(self):
        if len(str(self.economic_utility)) < 2 or len(str(self.economic_utility)) > 2:
            msg = 'El CI debe tener 11 dígitos'
            raise ValidationError(msg)

    def __str__(self):
        return 'Proyecto:{}--- Recurso:{}'.format(self.project, self.resource)


class Transition(models.Model):
    user_giver = models.ForeignKey(Profile, verbose_name='Dador', on_delete=models.CASCADE)
    user_receiver = models.ForeignKey(User, verbose_name='Receptor', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='Proyecto Trasladado', on_delete=models.CASCADE)
    category_new = models.IntegerField(verbose_name='Nueva categoria', null=True, blank=True)
    time_is_over = models.DateField(verbose_name='Hasta cuando')
    destroy = models.BooleanField(default=True, verbose_name='Acabar tiempo')

    def __str__(self):
        return 'De:{}, A:{}'.format(self.user_giver, self.user_receiver)

    def destroyed(self):
        today = datetime.today()
        rest = self.time_is_over.day-today.day
        if rest == 0:
            self.destroy = True
        return 'Faltan:{}----{}'.format(self.destroy, self.time_is_over.day-today.day)

