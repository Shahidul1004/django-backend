from django.shortcuts import render
from allauth.account.views import SignupView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class AccountSignupView(SignupView):
    template_name = "accounts/signup.html"


account_signup_view = AccountSignupView.as_view()


@login_required
def profile(request):
    user = request.user
    return render(request, "accounts/profile.html", {"user": user})


def helloView(request):
    redirect_url = "/accounts/login"
    return redirect(redirect_url)
    content = {"message": "Hello, World!"}
    your_json = [{"key1": 1, "key2": 2}]
    return HttpResponse(your_json, "application/json")
