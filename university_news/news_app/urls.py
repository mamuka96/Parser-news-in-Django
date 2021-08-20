from django.conf.urls import url
from django.urls import path
from . import parser
from . views import ContactsView, LoginView, CreateView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('contacts/', ContactsView.as_view()),
    path('', parser.home, name='home'),
    url('accounts/register/', CreateView.as_view(), name="register"),


]
