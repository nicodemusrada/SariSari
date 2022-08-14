from django.urls import path
from . import views
from . views import Login
app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', Login.as_view(), name='login')
]