from django.urls import path
from . import views
#from . significa que estou importando tudo o que tem dentro de views.py
urlpatterns = [
    path('', views.index, name='index')
]