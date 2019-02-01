from django.urls import path
from . import views


urlpatterns = [
 path('events',views.EventsList.as_view(),name='eventlist'),
]