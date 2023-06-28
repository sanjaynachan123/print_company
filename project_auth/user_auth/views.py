from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . import models
from .forms import CompanySetupForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.decorators.csrf import csrf_protect
from .helper import update_path
from .permissions import IsAdmin
# Create your views here.

def initial_company_setup(request):
    print(request.method)
    template_name='user_auth/setup.html'
    if request.method == 'POST':
        form = CompanySetupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('saved') #create a success page...!!
    form = CompanySetupForm()
    context={'form':form}
    return render(request, template_name,
                  context)
   
@csrf_protect
def login_view(request):
    print('method checking',request.method)
    form=LoginForm(request)
    if request.method == 'POST':
        form = LoginForm(request,request.POST)

        if form.is_valid():
            print('valid form')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)
            user = authenticate(request, username=username, password=password)
            # print('user',user)
            if user is not None:
                login(request, user)
                print('login successful')
                return redirect('home')  # Replace 'home' with the name of your home page URL
            else:
                form.add_error(None, 'Invalid username or password.')
        else:
            print('invalid form',form.errors)        
    
    return render(request, 'registration/login.html', {'form': form})
    


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'user_auth/signup.html' 
    

    
       
    
