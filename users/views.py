from django.http import HttpResponse
from django.template import loader

# Create your views here.

def users(request):
    template = loader.get_template('myFirst.html')
    return HttpResponse(template.render())
