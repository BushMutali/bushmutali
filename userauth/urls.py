from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('update/', views.user_update, name="update-user"), 
    
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="userauth/password_reset.html"), name="reset_password"),
    
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="userauth/password_reset_sent.html"), name="password_reset_done"),
    
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="userauth/password_reset_form.html"), name="password_reset_confirm"),
    
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="userauth/password_reset_done.html"), name="password_reset_complete"),
]
