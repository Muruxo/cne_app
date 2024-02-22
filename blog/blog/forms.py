from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from allauth.account.forms import LoginForm,SignupForm,ChangePasswordForm,SetPasswordForm,ResetPasswordForm,ResetPasswordKeyForm


class UserLoginForm(LoginForm):
    def _init_(self, *args, **kwargs):
        super(UserLoginForm, self)._init_(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Enter Username','id':'username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2 position-relative','placeholder':'Enter Password','id':'password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        
class UserRegistrationForm(SignupForm):
    def _init_(self, *args, **kwargs):
        super(UserRegistrationForm, self)._init_(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2','placeholder':'Enter Email','id':'email'})
        self.fields['email'].label="Email"
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Enter Username','id':'username1'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter Password','id':'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter Confirm Password','id':'password2'})
        self.fields['password2'].label="Confirm Password"
        
class PasswordChangeForm(ChangePasswordForm):
      def _init_(self, *args, **kwargs):
        super(PasswordChangeForm, self)._init_(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['oldpassword'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter currunt password','id':'password3'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter new password','id':'password4'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter confirm password','id':'password5'})
        self.fields['oldpassword'].label="Currunt Password"
        self.fields['password2'].label="Confirm Password"
        
class PasswordSetForm(SetPasswordForm):
      def _init_(self, *args, **kwargs):
        super(PasswordSetForm, self)._init_(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter new password','id':'password8'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter confirm password','id':'password9'})
        self.fields['password2'].label="Confirm Password"

class PasswordResetForm(ResetPasswordForm):
      def _init_(self, *args, **kwargs):
        super(PasswordResetForm, self)._init_(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2','placeholder':' Enter Email','id':'email1'})
        self.fields['email'].label="Email"
        
class PasswordResetKeyForm(ResetPasswordKeyForm):
      def _init_(self, *args, **kwargs):
        super(PasswordResetKeyForm, self)._init_(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter new password','id':'password6'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter confirm password','id':'password7'})
        self.fields['password2'].label="Confirm Password"