from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserEditSerializer, UserPasswordChangeSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class APIChangePasswordView(UpdateAPIView):
    
    def update(self, request, *args, **kwargs):
        serializer = UserPasswordChangeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # as drf authtoken is being used, create a new token upon password update
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        token, created = Token.objects.get_or_create(user=user)
        #return a new token
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response ({
            'token': token.key,
            'user_id': user.pk,
        })


class CustomUserList(APIView):
    def get(self, request):
        if not request.user.is_staff:
            return Response(
                {"message": "You do not have permission to view these records"},
                status=status.HTTP_403_FORBIDDEN
            )
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            accepted_terms = serializer.validated_data.get('accepted_terms')
            if accepted_terms:
                serializer.save()
                return Response(serializer.data)
            return Response({"detail": "You must accept the terms and conditions."},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                
      
    
class CustomUserDetail(APIView):
    def get_object(self, username):
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, username):
        user = self.get_object(username)

        if user != request.user and not request.user.is_staff:
            return Response(
                {"message": "You are not authorized to view this record"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):
        user = self.get_object(username)

        if user != request.user and not request.user.is_staff:
            return Response(
                {"message": "You are not authorized to edit this record"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = CustomUserEditSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = self.get_object(username)

        if user != request.user and not request.user.is_staff:
            return Response(
                {"message": "You are not authorized to delete this record"},
                status=status.HTTP_403_FORBIDDEN
            )
        user.delete()
        return Response({"message: User successfully deleted"}, status=status.HTTP_200_OK)