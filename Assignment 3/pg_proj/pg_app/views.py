from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import TeamMember
from django.shortcuts import render, redirect
from .models import Task
from django.utils.html import escape

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
    user_tasks = None
    if request.user.is_authenticated:
        user_tasks = Task.objects.filter(user=request.user)
    return render(request, 'pg_app/home.html', {'user_tasks': user_tasks})

def about(request):
    member1 = TeamMember('Damon Zhang', 's364662', 's364662@students.cdu.edu.au')
    member2 = TeamMember('Matt Bonfanti', 's349051', 's349051@students.cdu.edu.au')
    team_members = [member1, member2]

    context = {'team_members': team_members}
    return render(request, 'pg_app/about.html', context)

def create_task(request):
    if request.method == 'POST':
        title = escape(request.POST.get('title', ''))
        description = escape(request.POST.get('description', ''))
        new_task = Task(
            title = title,
            description = description,
            user = request.user)
        new_task.save()
        return redirect('home')
    return render(request, 'create_task.html')

def mark_task_complete(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.delete()
    return redirect('home')

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})