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

def dayNumber(request, dayinweek_number):
    days_names = list(list_of_days.keys())

    if dayinweek_number > len(days_names):
        return HttpResponseNotFound('Zadali jse spatne cislo dne')
    
    redirect_day = days_names[dayinweek_number - 1]
    redirect_path = reverse('days_tasks', args = [redirect_day])
    return HttpResponseRedirect(redirect_path)


def dayText(request, dayinweek_string):
    day_description = ''
    if dayinweek_string == 'monday':
        day_description = 'Pondeli'
    elif dayinweek_string == 'tuesday':
        day_description = 'Utery'
    elif dayinweek_string == 'wednesday':
        day_description = 'Streda'
    elif dayinweek_string == 'thursday':
        day_description = 'Ctvrtek'
    elif dayinweek_string == 'friday':
        day_description = 'Patek'
    elif dayinweek_string == 'saturday':
        day_description = 'Sobota'
    elif dayinweek_string == 'sunday':
        day_description = 'Nedele'
    else:
        return HttpResponseNotFound('Neexistujisi den')
    return HttpResponse(day_description)

# lesson 25