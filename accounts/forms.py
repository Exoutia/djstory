from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=50, required=True)

class RegisterForm(forms.Form):
    firstname = forms.CharField(label="First Name", max_length=50, required=True)
    lastname = forms.CharField(label="Last Name", max_length=50, required=True)
    username = forms.CharField(label="Username", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=50, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", max_length=50, required=True)
    
        