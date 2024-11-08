from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
list_of_days = {
    'monday': 'Jit nakoupit',
    'tuesday': 'Ucit se Python',
    'wednesday': 'Vynest kos',
    'thursday': 'Dojit nakoupit',
    'friday': 'Naprogramovat hru',
    'saturday': 'Zajit do kina',
    'sunday': 'Jit cvicit',
}

def index(request):
    content = ''
    days = list(list_of_days.keys())

    content = '<ul>'
    for one_day in days:
        url = reverse('days_tasks', args = [one_day])
        content += f'<li><a href="{url}">{one_day.capitalize()}</a></li>'
    content += '</ul>'
    
    return HttpResponse(content)

def dayNumber(request, dayinweek_number):
    days_names = list(list_of_days.keys())

    if dayinweek_number > len(days_names):
        return HttpResponseNotFound('Zadali jse spatne cislo dne')
    
    redirect_day = days_names[dayinweek_number - 1]
    redirect_path = reverse('days_tasks', args = [redirect_day])
    return HttpResponseRedirect(redirect_path)


def dayText(request, dayinweek_string):
    try:
        task = list_of_days[dayinweek_string]
        formated_task = f'<h1>{task}</h1>'
        return HttpResponse(formated_task)
    except:
        return HttpResponseNotFound('Error, not Found')