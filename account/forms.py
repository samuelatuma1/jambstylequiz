from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
	username = forms.CharField(max_length=60)
	password = forms.CharField(max_length=60, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Input Password',
										 widget=forms.PasswordInput)
										 
	password2 = forms.CharField(label='Retype Password',
										 widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name')
		
	def verify_password(self):
		password1 = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		
		
		
		if password1 != password2:
			raise forms.ValidationError("Passwords don't  match")
			
		elif password1 < 6:
			raise forms.ValidationError('Password must be at least six characters 																		long')
		else:
			return password1
			
			
class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields =['first_name', 'last_name', 'email']
		
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['date_of_birth', 'photo']