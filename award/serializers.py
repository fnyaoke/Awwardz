from rest_framework import serializers
from .models import *

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['author', 'image', 'description', 'date_created', 'title', 'link', 'author_profile']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'biography', 'created', 'modified']

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ['author', 'author_profile']