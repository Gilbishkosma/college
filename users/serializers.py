from rest_framework import serializers
from .models import CustomUser
from project.utils import validate_password


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   CustomUser
        fields  =   ('username','password','College')

    def validate(self, data):
        t_data=super(SignupSerializer,self).validate(data)
        if CustomUser.objects.filter(username=t_data.get('username')).exists():
            raise serializers.ValidationError("A user with this name already exist")
        else:
            status,msg=validate_password(t_data.get('password'))
            if not status:
                raise serializers.ValidationError(msg)
        return t_data


class UserSerializer(serializers.ModelSerializer):
      class Meta:
        model = CustomUser
        fields = ('id','username','College','email')