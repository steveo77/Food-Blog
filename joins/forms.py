from django import forms

from .models import Join

from django.contrib.auth import get_user_model

User = get_user_model()

class EmailForm(forms.Form):
	username = forms.CharField(required=False)
	email = forms.EmailField()
	password = forms.EmailField(widget=forms.PasswordInput())


class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ["email",]


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
		return username
