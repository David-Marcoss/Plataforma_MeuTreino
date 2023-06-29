from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import cadastroview,cadastroview2


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('cadastro-user/',cadastroview,name='cadastro-user'),
    path('cadastro-user2/<int:pk>',cadastroview2.as_view(),name='cadastro-user2'),
    
]
