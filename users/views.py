from django.http import HttpResponse
from django.template import loader
from .models import Users
# Create your views here.

def users(request):
    myUsers = Users.objects.all().values()
    template = loader.get_template('myFirst.html')
    context = {
        'myUsers':myUsers,
    }
    return HttpResponse(template.render(context, request))
