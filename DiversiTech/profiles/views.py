from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Industry, Tag, Experience
from .serializers import (ProfileSerializer, ProfileDetailSerializer,
     IndustrySerializer, TagSerializer, ExperienceSerializer, ExperienceDetailSerializer)
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrAdminOrReadOnly


class TagList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            tag = Tag.objects.get(pk=pk)
            return tag
        except Tag.DoesNotExist:
            raise Http404
    
    def get(self, request):
        tags = Tag.objects.all().order_by('tag_name')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if not request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN
            )
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
                {"detail": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN
            )
        tag = self.get_object(pk)
        tag.delete()
        return Response({"detail": "Tag successfully deleted"},
                        status=status.HTTP_200_OK)

class IndustryList(APIView):

    def get_object(self, pk):
        try:
            industry = Industry.objects.get(pk=pk)
            return industry
        except Industry.DoesNotExist:
            raise Http404
    
    def get(self, request):
        industries = Industry.objects.all().order_by('industry_name')
        serializer = IndustrySerializer(industries, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if not request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN
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
                {"detail": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN
            )
        industry = self.get_object(pk)
        industry.delete()
        return Response({"message": "Industry category successfully deleted"},
                        status=status.HTTP_200_OK)


class ProfileList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    # this method gets all Profiles from the DB and then filters by the user who submits a request
    # if there is a profile with the owner id = request.user.id the method returns True and otherwise False
    def profile_exists(self, owner):
        profiles = Profile.objects.all()
        profile= profiles.filter(owner=owner)
        if profile:
            return True
        else:
            return False

    def post(self, request):
    #   checking if the user already have a profile
      if not self.profile_exists(owner=request.user.id):
        # if not - execute the normal post request
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )
      else:
        # else throw an error
        return Response(
                 {"detail": "You already have a profile."}, status=status.HTTP_403_FORBIDDEN)
          

class ProfileDetail(APIView): 
    permission_classes = [
        IsOwnerOrAdminOrReadOnly
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
        return Response({"detail":"Profile deleted successfully"}, status=status.HTTP_200_OK)



class ExperienceList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
    def get(self, request, profile_id=None):
        if profile_id:
            experiences = Experience.objects.all().filter(profile=profile_id)
        else:
            experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

    

    def post (self,request, profile_id):
        serializer = ExperienceSerializer(data=request.data)
            
        if serializer.is_valid():
            serializer.save(profile=profile_id)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ExperienceDetail(APIView): 
# will need to add the endpoint in URLs.py
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsSupporterOrReadOnly
    # ]

# getting the object from the database
    def get_object(self, pk):
        try:
            experience=Experience.objects.get(pk=pk)
            self.check_object_permissions(self.request, experience)
            return experience
        except Experience.DoesNotExist:
            raise Http404
        
# passing the object to the serializer and returning serialized data
    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(experience)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put (self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
             instance=experience,
             data=request.data,
             partial=True
        )
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(
             serializer.errors,
             status=status.HTTP_400_BAD_REQUEST
        )    
