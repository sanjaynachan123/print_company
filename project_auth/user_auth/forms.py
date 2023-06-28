from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from .helper import update_path
class CompanySetupForm(forms.ModelForm):
    class Meta:
        model = models.FileDrive
        fields = '__all__'
        
    def save(self, commit=True):
      path = self.cleaned_data['location'] 
      new_path = 'r' + repr(path)
      self.cleaned_data['location'] = new_path
      instance = super().save(commit=False) 
      if commit:
          instance.save()
      return instance

# class CompanySetupForm(forms.Form):
#      location = forms.CharField(label='location',max_length=255)
#      filedrive = forms.FileField()
     
class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = models.CustomUser
        fields = ('username', 'mobile_number', 'birth_date','roles')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = models.CustomUser
        fields = ('username', 'mobile_number', 'birth_date','roles')       

class LoginForm(AuthenticationForm):

    class Meta:
        fields = ('username', 'password')       