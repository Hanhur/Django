from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'bookapp/index.html')

def register(request):
    if request.method == 'POST':
        # vezmi data z formuláře, validuj a ulož do tabulky auth_user
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-url') # po registraci přesměrujme na přihlášení
    else:
        form = RegistrationForm()
        return render(request, 'bookapp/register.html', {
            'form': form,
        })
    
@login_required
def dashboard(request):
    return render(request, 'bookapp/dashboard.html')

@login_required
def protected_page(request):
    return render(request, 'bookapp/protected-page.html')