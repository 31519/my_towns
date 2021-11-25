from rest_framework import serializers
from news_api_app.serializers import UserSerializers, RegistrationSerializer, UserSerializerWithToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def UserList(request):
    user = User.objects.all()
    serializer = UserSerializers(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserProfile(request):
    user = request.user
    serializer = UserSerializers(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def UserRegistration(request):
    if request.method == 'POST':
        serializers = RegistrationSerializer(data=request.data)

        data ={}
        if serializers.is_valid():
            account = serializers.save()
            data['username'] = account.username
            data['email'] = account.email
            data['password'] = account.password
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        else:
            data = serializers.errors
        return Response(data)

# @api_view(['POST'])
# def UserRegistration(request):
#     data  = request.data
#     user = User.objects.create(
#         username=data['username'],
#         email = data['email'],
#         password = data['password'],
#         # password2 = data['password2']

#     )
#     serializer = RegistrationSerializer(user, many=False)
#     return Response(serializer.data)
