from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JokeForm
from jokesapp.models import Jokes

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
            joke = Jokes(
                user_name = form.cleaned_data['user_name'],
                joke_text = form.cleaned_data['joke_text'],
                rating = form.cleaned_data['rating'],
            )
            joke.save()
            return HttpResponseRedirect('/thank-you')

    form = JokeForm()
    return render(request, 'jokesapp/index.html', {
        'jokeForm': form,
    })

def thank_you(request):
    return render(request, 'jokesapp/thank-you.html')

def all_jokes(request):
    all_jokes = Jokes.objects.all()
    return render(request, 'jokesapp/all-jokes.html', {
        'all_our_jokes': all_jokes,
    })