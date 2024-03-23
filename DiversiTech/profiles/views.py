from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer, ProfileDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly

class ProfileList(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
     serializer = ProfileSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(
        serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
        )

class ProfileDetail(APIView): 
    permission_classes = [
        IsOwnerOrReadOnly
     ]

# getting the object from the database
    def get_object(self, pk):
        try:
            profile=Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
        
# passing the object to the serializer and returning serialized data
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileDetailSerializer(profile)
        return Response(serializer.data)
    
    def put (self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileDetailSerializer(
             instance=profile,
             data=request.data,
             partial=True
        )
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        
        return Response(
             serializer.errors,
             status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self,request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response({"message":"Profile deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
          