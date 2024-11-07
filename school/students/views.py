from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

students_info = {
    'harmiona': 'Hermiona je ...',
    'david': 'David jr ...',
    'harry': 'Harry je ...',
    'ron': 'Ron je ...',
}

# Create your views here.

def allstudentsinfo(request, studentsname):
    try:
        result_info = students_info[studentsname]
        return HttpResponse(result_info)
    except:
        return HttpResponseNotFound('Zadano spatne jmeno')

# def davidStudents(request):
#     return HttpResponse('Informace o Davidovi')

# def harryStudents(request):
#     return HttpResponse('Informace o Harrym')

# def hermionaStudents(request):
#     return HttpResponse('Infornamace o Hermione')

# def ronStudents(request):
#     return HttpResponse('Informace o Ronovi')