from rest_framework import serializers
from .models import Events,Participant


class EventSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = Events
	 	fields = "__all__"

class ParticipantSerializer(serializers.ModelSerializer):
	 event = serializers.PrimaryKeyRelatedField(many=True ,read_only=True)
	 class Meta:
	 	model = Participant
	 	fields = ('id','event','payment')

