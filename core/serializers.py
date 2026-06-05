from rest_framework import serializers

from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'description',
            'email',
            'image_profile_url',
            'course',
            'linkend',
            'git',
        ]