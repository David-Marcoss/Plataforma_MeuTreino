from django.urls import include, path
from .views import *

urlpatterns = [
    path('exercicios/',ListExerciciosView.as_view(),name='exercicios'),
    path('exercicios/user/',ListExerciciosUserView.as_view(),name='exercicios-user'),
    path('exercicios/create/',CreateExercicioView.as_view(),name='exercicios-create'),
    path('exercicios/update/<int:pk>/',UpdateExerciciosView.as_view(),name='exercicios-update'),
    path('exercicios/delete/<int:pk>/',DeleteExerciciosView.as_view(),name='exercicios-delete'),
    path('exercicios/detail/<int:pk>/',DetailExerciciosView.as_view(),name='exercicios-detail'),
    path('treinos/create/',CreateTreinoView,name='treinos-create'),
    path('treinos/create/exercicios/<int:pk>/',CreateExerciciosTreino,name='treinos-create-exercicios'),
    path('treinos/',ListTreinosView.as_view(),name='treinos'),
    path('treinos/user/',ListTreinosUserView.as_view(),name='treinos-user'), 
    
    
]