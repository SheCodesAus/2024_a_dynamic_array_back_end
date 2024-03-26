from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Industry, Tag
from .serializers import ProfileSerializer, ProfileDetailSerializer, IndustrySerializer, TagSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly


class TagList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            tag = Tag.objects.get(pk=pk)
            return tag
        except Tag.DoesNotExist:
            raise Http404
    
    def get(self, request):
        tags = Tag.objects.all().order_by('title')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"message": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN
            )
        tag = self.get_object(pk)
        tag.delete()
        return Response({"message": "Tag successfully deleted"},
                        status=status.HTTP_200_OK)

class IndustryList(APIView):

    def get_object(self, pk):
        try:
            industry = Industry.objects.get(pk=pk)
            return industry
        except Industry.DoesNotExist:
            raise Http404
    
    def get(self, request):
        industries = Industry.objects.all().order_by('title')
        serializer = IndustrySerializer(industries, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if not request.user.is_staff:
            return Response(
                {"message": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN
            )
        serializer = IndustrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"message": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN
            )
        industry = self.get_object(pk)
        industry.delete()
        return Response({"message": "Industry category successfully deleted"},
                        status=status.HTTP_200_OK)


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
          