from django import forms
from accounts.models import CustomUser

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'birthYear')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthYear = self.cleaned_data['birthYear']
        user.save()

        # user.profile.nationality = self.cleaned_data['nationality']
        # user.profile.gender = self.cleaned_data['gender']
        # user.profile.save()