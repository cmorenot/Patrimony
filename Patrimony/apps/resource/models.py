from django.db import models
# Create your models here.

TYPE = (
    (0, 'Local público y privado'),
    (1, 'Local privado'),
    (2, 'Local público'),
    (3, 'Espacio público'),
    (4, 'Arqueológico'),

)

PROTECTION_GRADE = (
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
)


class Resource(models.Model):
    def url(self, filename):
        url = 'Outline/%s/%s' % (self.name, filename)
        return url

    def url_img(self, filename):
        url = 'ImageStart/%s/%s' % (self.name, filename)
        return url

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    existing_use = models.TextField(verbose_name='Uso Actual')
    direction = models.TextField(verbose_name='Localizacion')
    description = models.TextField(verbose_name='Características generales')
    reference_time = models.DateField(verbose_name='Epoca de referencia')
    alternative_of_use = models.TextField(verbose_name='Alternativa de uso')
    other_values = models.TextField(verbose_name='Otros valores')
    outline = models.ImageField(verbose_name='Croquis', upload_to=url)
    image = models.ImageField(verbose_name='Imagen', upload_to=url_img)
    protection_grade = models.SmallIntegerField(choices=PROTECTION_GRADE, verbose_name='Grado de proteccion')
    type = models.IntegerField(choices=TYPE, verbose_name='Tipo', null=True, blank=True)

    def __str__(self):
        return self.name


class FixingActions(models.Model):
    def url(self, filename):
        url = 'fixingActions/%s/%s/%s/%s' % (self.resource, self.user, self.time, filename)
        return url

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.CharField(max_length=200, verbose_name='Usuario')
    images = models.ImageField(verbose_name='Imagen de la Accion correctiva', upload_to=url)
    time = models.DateField(verbose_name='Fecha de la accion correctiva')
    description = models.TextField('Descripcion de la acción correctiva')

    def __str__(self):
        return 'Acción Corectiva:{},Tiempo:{}'.format(self.resource, self.time)


class Threats(models.Model):
    description = models.TextField(verbose_name='Descripción')
    type = models.CharField(max_length=200, verbose_name='Tipo')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class Imagen(models.Model):
    def url(self, filename):
        url = 'ImageSecondary/%s/%s' % (self.resource, filename)
        return url

    name = models.ImageField(verbose_name='Nombre', upload_to=url)
    resource = models.ForeignKey(Resource, verbose_name='Recurso', on_delete=models.CASCADE)


class GeoLocalization(models.Model):
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, verbose_name='Recurso al que pertenece esta Geolocalización')

    def __str__(self):
        return '({}-{})'.format(self.lat, self.lng)


class Area(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    resource = models.ManyToManyField(Resource, verbose_name='Recursos que integran un Área')

    def __str__(self):
        return '{}-{}'.format(self.name, self.pk)
