from django.urls import path
from . import views
urlpatterns = [
  path('signup',views.Signup.as_view(),name="signup"),
  path('login',views.UserLogin.as_view(),name='login'),
  path('profile',views.UserProfile.as_view(),name="userprofile"),  
]