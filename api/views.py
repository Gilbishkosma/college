from django.shortcuts import render
from events.models import Events,Participant,Coordinator
from rest_framework.views import APIView
from rest_framework import generics,permissions
from rest_framework.response import Response
from events.serializers import EventSerializer
# Create your views here.


class EventsList(generics.ListAPIView):
	queryset = Events.objects.all()
	serializer_class = EventSerializer
	permission_classes = (permissions.AllowAny,) 

