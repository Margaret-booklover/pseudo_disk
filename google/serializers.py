from google.models import Folder, File
from rest_framework import serializers
from django.contrib.auth.models import User


class FolderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    parents = serializers.PrimaryKeyRelatedField(many=True, queryset=Folder.objects.all())

    class Meta:
        model = Folder
        fields = ['id', 'folder_name', 'parents', 'owner']


class FileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ['id', 'filename', 'mime_type', 'size', 'created_at']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

