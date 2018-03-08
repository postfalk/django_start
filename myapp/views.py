from django.http import HttpResponse
from myapp.models import Person


def current_datetime(request):
    html = '<html><body>'
    for person in Person.objects.all():
        html += '{} {} {}'.format(person.first_name, person.last_name, person.profession.name)
    html += '</body></html>'
    return HttpResponse(html)
