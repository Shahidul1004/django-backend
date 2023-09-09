from django.shortcuts import render
from allauth.account.views import SignupView
from django.http import HttpResponse

class AccountSignupView(SignupView):
    # Signup View extended

    # change template's name and path
    template_name = "accounts/signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...


account_signup_view = AccountSignupView.as_view


def helloView(request):
    content = {"message": "Hello, World!"}
    your_json = [{'key1': 1, 'key2': 2}]
    return HttpResponse(your_json, 'application/json')