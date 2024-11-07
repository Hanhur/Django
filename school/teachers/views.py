from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

teachers_info = {
    'snape': 'Ucitel Snape',
    'brumbal': 'Ucitel Brumbal',
    'mcgonagallova': 'Ucitelka McGonagallova',
}
# Create your views here.
def allTeachersAll(request, teachersname):
    try:
        info = teachers_info[teachersname]
        return HttpResponse(info)
    except:
        return HttpResponseNotFound('Error, not Found')