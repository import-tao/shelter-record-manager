
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('profile/', views.userProfileView, name='user_profile'),
    path('profile/edit/', views.userEditView, name='user_profile_edit'),
    path('profile/password/', views.change_password, name='password_update'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]