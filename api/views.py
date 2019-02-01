from django.shortcuts import render
from events.models import Events,Participant,Coordinator
from users.models import CustomUser
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import generics,permissions
from rest_framework.response import Response
from events.serializers import EventSerializer,ParticipantSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from users.api_permissions import CustomTokenAuthentication
from rest_framework.status import HTTP_200_OK
# Create your views here.


class EventsList(generics.ListAPIView):
	queryset = Events.objects.all()
	serializer_class = EventSerializer
	permission_classes = (permissions.AllowAny,) 

class EventEnrolled(APIView):
      permission_classes=(IsAuthenticated,)
      authentication_classes= (CustomTokenAuthentication,)
      def get(self,request):
         events = Participant.objects.all().filter(user=request.user)
         serializer = ParticipantSerializer(events,many=True)
         return Response(serializer.data)
      def post(self,request):
          response_dict={'success':False}
          eid = request.data.get('event_id')
          if eid:
             event = Events.objects.filter(id=eid)
             if event:
                  event = event[0]
             else:
                response_dict['reason']="Event not found"
                return Response(response_dict,HTTP_200_OK)
             checkpart = Participant.objects.all().filter(Q(user=request.user) & Q(event=event))
             if checkpart:
                 response_dict['reason']="Already registered in this event"
                 return Response(response_dict,HTTP_200_OK)
             participate = Participant(user=request.user,event=event,payment=False)
             participate.save()
          else:
             response_dict['reason']="Event ID is missing"
             return Response(response_dict,HTTP_200_OK)
          response_dict['success']=True
          return Response(response_dict,HTTP_200_OK)


