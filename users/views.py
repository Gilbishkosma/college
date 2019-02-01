from .models import CustomUser,Token
from .serializers import SignupSerializer,UserSerializer
from rest_framework.views import APIView
from project.utils import get_error
from .api_permissions import CustomTokenAuthentication
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated,AllowAny

class Signup(APIView):
    permission_classes=(AllowAny,)
    authentication_classes=tuple()
    
    def post(self,request):
        response_dict={'success':False}
        user_data=request.data.get('user_data',{})
        if user_data == {}:
            response_dict['reason'] = "user_data is missing"
            return Response(response_dict,HTTP_200_OK)
        serializer=SignupSerializer(data=user_data)
        if serializer.is_valid():
            u_data=serializer.validated_data
            customer=CustomUser(**u_data)
            customer.set_password(user_data.get('password'))
            customer.save()
            response_dict['success']=True
            return Response(response_dict,HTTP_200_OK)
        else:
            response_dict['reason']=get_error(serializer)
            return Response(response_dict,HTTP_200_OK)

class UserLogin(APIView):
    permission_classes=(AllowAny,)
    authentication_classes=tuple()
    #It returns token and you have to use the token in all places to indicate that user is logged in
    def post(self,request):
        response_dict={'success':False}
        user_data=request.data.get('user_data',{})
        if user_data == {}:
            response_dict['reason'] = "user_data is missing"
            return Response(response_dict,HTTP_200_OK)
        name=user_data.get('username')
        if not name:
            response_dict['reason']='Username cannot be empty'
            return Response(response_dict,HTTP_200_OK)
        user = CustomUser.objects.filter(username=name)
        if user:
            user = user[0]
        else:
            response_dict['reason']='User cannot be found'
            return Response(response_dict,HTTP_200_OK)
        password = user_data.get('password')
        if password:
           if not user.check_password(password):
              response_dict['reason']='Invalid credentials'
              return Response(response_dict,HTTP_200_OK)
        else:
            response_dict['reason']="Password can't be empty"
            return Response(response_dict,HTTP_200_OK)
        token,c=Token.objects.get_or_create(user=user)
        response_dict['success']=True
        response_dict['token'] = token.key
        return Response(response_dict,HTTP_200_OK)


class UserProfile(APIView):
      permission_classes=(IsAuthenticated,)
      authentication_classes= (CustomTokenAuthentication,)
      def get(self,request):
         user = CustomUser.objects.all().filter(id=request.user.id)[0]
         serializer = UserSerializer(user)
         return Response(serializer.data)
      
      def post(self,request):
         response_dict={'success':False}
         uid = request.data.get('id')
         name = request.data.get('username')
         college = request.data.get('college')
         if uid:
            user = CustomUser.objects.filter(id=uid)
            if user:
                user = user[0]
                if user != request.user:
                    response_dict['reason']="You don't have permissions to access this data"
                    return Response(response_dict,HTTP_200_OK)
            else:
                response_dict['reason']="User not found"
                return Response(response_dict,HTTP_200_OK)
            if name:
                try:
                   tempuser = CustomUser.objects.all().filter(username=name)[0]
                   if tempuser:
                    response_dict['reason']="Username already taken"
                    return Response(response_dict,HTTP_200_OK)
                except:
                   user.username = name    
            if college : user.College = college
            user.save() 
         else:
            response_dict['reason']="ID is missing"
            return Response(response_dict,HTTP_200_OK)
         response_dict['success'] = True
         return Response(response_dict,HTTP_200_OK)