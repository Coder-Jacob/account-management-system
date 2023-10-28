from django.urls import path
from . import views

app_name = 'AMS'
urlpatterns = [
    path('getac', views.Accounts.as_view()),
    path('', views.editAccount, name='editAccount'),
]
