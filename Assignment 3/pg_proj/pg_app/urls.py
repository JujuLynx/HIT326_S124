from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='pg_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pg_app/logged_out.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
