from django.shortcuts import render
from allauth.account.views import SignupView


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


account_signup_view = AccountSignupView.as_view()