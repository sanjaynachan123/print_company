from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,FileDrive
from .forms import MyUserCreationForm, MyUserChangeForm


class MyUserAdmin(UserAdmin):
    
    # add_form = MyUserCreationForm
    # form = MyUserChangeForm
    list_display = ['username', 'mobile_number', 'birth_date','roles']
admin.site.register(CustomUser,MyUserAdmin)
admin.site.register(FileDrive)
