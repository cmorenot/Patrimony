from django.contrib import admin
from .models import Project, Evaluation, Transition
# Register your models here.


admin.site.register(Project)
admin.site.register(Evaluation)
admin.site.register(Transition)
