from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JokeForm

# Create your views here.
def jokes(request):
    # if request.method == "POST":
    #     visiter_name = request.POST["username"]
    #     if visiter_name == '':
    #         return render(request, 'jokesapp/index.html', {
    #             'empty_username': True,
    #         })
    #     return HttpResponseRedirect('/thank-you')

    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thank-you')

    form = JokeForm()
    return render(request, 'jokesapp/index.html', {
        'jokeForm': form,
    })

def thank_you(request):
    return render(request, 'jokesapp/thank-you.html')