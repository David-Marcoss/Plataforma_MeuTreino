from django.urls import include, path
from .views import *

urlpatterns = [
    path('dietas/refeicoes/',ListReceitasView.as_view(),name='receitas'),
    path('dietas/refeicoes/create/',CreateReceitasView.as_view(),name='refeicao-create'),
    path('dietas/refeicoes/user/',ListReceitasUserView.as_view(),name='receitas-user'),
    path('dietas/refeicoes/update/<int:pk>/',UpdateReceitasView.as_view(),name='refeicao-update'),
    path('dietas/refeicoes/delete/<int:pk>/',DeleteReceitasView.as_view(),name='refeicao-delete'),
    path('dietas/refeicoes/detail/<int:pk>/',DetailReceitasView.as_view(),name='receitas-detail'),
    
]