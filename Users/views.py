from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Account
from django.views import View
from .forms import LoginForm, SignupForm


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, "Users/index.html", {'user': request.user, 'form': LoginForm})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "Users/index.html", {'user': request.user, 'form': LoginForm, 'failed': True})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class Signup(View):
    def get(self, request):
        signup_form = SignupForm
        return render(request, "Users/signup.html", {'form': signup_form})

    def post(self, request):
        post_data = request.POST
        signup_form = SignupForm(post_data)

        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.set_password(signup_form.cleaned_data['password'])
            user.save()
            account = Account(user=user)
            account.save()

            return redirect("/")
        else:
            return render(request, "Users/signup.html", {'form': signup_form})
