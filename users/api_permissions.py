from rest_framework.authentication import TokenAuthentication
from .models import Token



class CustomTokenAuthentication(TokenAuthentication):
    model = Token
