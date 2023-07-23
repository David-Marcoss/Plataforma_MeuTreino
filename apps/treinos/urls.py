from django.urls import include, path
from .views import *

urlpatterns = [
    path('treinos/',treinosView,name='treinos'),
    path('exercicios/',ListExerciciosView.as_view(),name='exercicios'),
    path('exercicios/user/',ListExerciciosUserView.as_view(),name='exercicios-user'),
    path('exercicios/create/',CreateExercicioView.as_view(),name='exercicios-create'),
    path('exercicios/update/<int:pk>/',UpdateExerciciosView.as_view(),name='exercicios-update'),
    path('exercicios/delete/<int:pk>/',DeleteExerciciosView.as_view(),name='exercicios-delete'),
    
    
]