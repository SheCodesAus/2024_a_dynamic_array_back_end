from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileDetailSerializer (ProfileSerializer):
    # pledges = PledgeSerializer(many=True, read_only=True)
    # total_number_of_pledges = serializers.ReadOnlyField()
    # sum_of_pledges = serializers.ReadOnlyField()
     slug_field = "username"
     def update(self, instance, validated_data):
        
        instance.bio = validated_data.get('bio', instance.bio)
        instance.location = validated_data.get('location', instance.location)
        instance.picture_url = validated_data.get('picture_url', instance.picture_url)
        instance.is_hidden = validated_data.get('is_hidden', instance.is_hidden)
        instance.number_of_endorsements = validated_data.get('number_of_endorsements', instance.number_of_endorsements)
        instance.email_url = validated_data.get('email_url', instance.email_url)
        instance.facebook_url = validated_data.get('facebook_url', instance.facebook_url)
        instance.instagram_url = validated_data.get('instagram_url', instance.instagram_url)
        instance.github_url = validated_data.get('github_url', instance.github_url)
        instance.linked_in_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.portfolio_url = validated_data.get('portfolio_url', instance.portfolio_url)
        instance.contact_preference = validated_data.get('contact_preference', instance.contact_preference)
        instance.is_open_to_mentor = validated_data.get('is_open_to_mentor', instance.is_open_to_mentor)
        instance.is_seeking_mentorship = validated_data.get('is_seeking_mentorship', instance.is_seeking_mentorship)
    
        instance.save()
        return instance