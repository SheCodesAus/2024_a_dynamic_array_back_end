from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer


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
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)

        if user != request.user and not request.user.is_staff:
            return Response(
                {"message": "You are not authorized to view this record"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)