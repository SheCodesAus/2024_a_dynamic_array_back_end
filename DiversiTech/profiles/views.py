from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProjectList(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfiletSerializer(profiles, many=True)
        return Response(serializer.data)