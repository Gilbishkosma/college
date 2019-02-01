from django.urls import path
from . import views


urlpatterns = [
 path('avesh/events',views.EventsList.as_view(),name='eventlist'),
 path('participant/enroll',views.EventEnrolled.as_view(),name="eventenrolled"),
]