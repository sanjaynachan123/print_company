from django.urls import path
from . import views
from .views import SignUpView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
    path('setup_1/',views.initial_company_setup,name='setup_1'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='user_auth/home.html'), name='home'),
    path('login/',views.login_view,name='login')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)