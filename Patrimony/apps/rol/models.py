from django.db import models
from django.urls import reverse


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

CATEGORY = (
    (0, 'Sin especificar'),
    (1, 'Ing. Civil'),
    (2, 'Geógrafo'),
    (3, 'Sociólogo'),
    (4, 'Demógragfo'),
    (5, 'Arquitecto'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.IntegerField(choices=CATEGORY, verbose_name='categoría', null=True, blank=True, default=0)
    boss = models.BooleanField(default=False, verbose_name='Jefe de proyecto')

    def __str__(self):
        return '%s' % self.user


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


