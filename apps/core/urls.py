from django.urls import include, path
from .views import homeView

urlpatterns = [
    path('',homeView,name='home'),
    #path('cadastro/',cadastroview.as_view(),name='cadastro'),
    
]