from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Task
from .forms import TaskForm

def register_view(request):

    if request.method == "POST":

        full_name = request.POST.get(
            "full_name"
        )

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        confirm_password = request.POST.get(
            "confirm_password"
        )

        if password != confirm_password:

            return render(
                request,
                "tasks/register.html",
                {
                    "error":
                    "Passwords do not match"
                }
            )

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                "tasks/register.html",
                {
                    "error":
                    "Username already exists"
                }
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        user.first_name = full_name

        user.save()

        login(
            request,
            user
        )

        return redirect(
            "dashboard"
        )

    return render(
        request,
        "tasks/register.html"
    )

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)

            messages.success(
                request,
                "Login successful!"
            )

            return redirect("dashboard")

        return render(
            request,
            "tasks/login.html",
            {
                "error": "Invalid username or password"
            }
        )

    return render(
        request,
        "tasks/login.html"
    )


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(
                request,
                "Task created successfully!"
            )

            return redirect("dashboard")

    else:
        form = TaskForm()

    search = request.GET.get("search", "")

    tasks = Task.objects.filter(
        user=request.user
    )

    if search:
        tasks = tasks.filter(
            title__icontains=search
        )

    todo_tasks = tasks.filter(
        stage="todo"
    )

    progress_tasks = tasks.filter(
        stage="progress"
    )

    done_tasks = tasks.filter(
        stage="done"
    )

    context = {
    "form": form,
    "search": search,

    "todo": todo_tasks,
    "progress": progress_tasks,
    "done": done_tasks,

    "todo_count": todo_tasks.count(),
    "progress_count": progress_tasks.count(),
    "done_count": done_tasks.count(),

    "all_tasks": tasks
    }
    return render(
        request,
        "tasks/dashboard.html",
        context
    )


@login_required
def delete_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    task.delete()

    messages.success(
        request,
        "Task deleted successfully!"
    )

    return redirect("dashboard")


@login_required
def move_task(request, pk, stage):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user
    )

    valid_stages = [
        "todo",
        "progress",
        "done"
    ]

    if stage in valid_stages:
        task.stage = stage
        task.save()

        messages.success(
            request,
            "Task status updated!"
        )

    return redirect("dashboard")