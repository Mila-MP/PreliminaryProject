from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home_page")
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, "registration/sign_up.html", context)
