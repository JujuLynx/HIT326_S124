from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import TeamMember

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def my_view(request):
    return render(request, 'pg_app/my_template.html')

@login_required
def profile(request):
    return render(request, 'pg_app/profile.html')

def home(request):
    return render(request, 'pg_app/home.html')

def about(request):
    member1 = TeamMember('Damon Zhang', 's364662', 's364662@students.cdu.edu.au')
    member2 = TeamMember('Matt Bonfanti', 's349051', 's349051@students.cdu.edu.au')
    team_members = [member1, member2]

    context = {'team_members': team_members}
    return render(request, 'pg_app/about.html', context)
