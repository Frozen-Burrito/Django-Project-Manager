from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup_page, name="signup"),

    path('profile/', views.user_profile, name="profile"),
    path('profile-edit/', views.user_profile_edit, name="profile-edit"),

    path('logout/', views.logoutUser, name="logout"),
]