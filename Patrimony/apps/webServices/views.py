from django.http import HttpResponse
from django.core.serializers import serialize
from apps.resource.models import Resource
from apps.rol.models import Profile,User
# Create your views here.


def resource_ws(request):
    data = serialize('json', User.objects.all())
    return HttpResponse(data)
