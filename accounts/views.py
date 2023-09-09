from django.shortcuts import render
from allauth.account.views import SignupView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class AccountSignupView(SignupView):
    template_name = "accounts/signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...


account_signup_view = AccountSignupView.as_view()


@login_required
def profile(request):
    user = request.user
    # If using a custom profile model, you can access user profile data like user.userprofile.bio
    return render(request, 'accounts/profile.html', {'user': user})


def helloView(request):
    content = {"message": "Hello, World!"}
    your_json = [{'key1': 1, 'key2': 2}]
    return HttpResponse(your_json, 'application/json')