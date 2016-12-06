from rest_framework_json_api import serializers
from rest_framework_json_api.relations import *

#load django and webapp models
from django.contrib.auth.models import *
from api.models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = Profile

class ClothSerializer(serializers.ModelSerializer):
	#user = UserSerializer(read_only=True)
	class Meta:
		model = Cloth
		fields = ('id', 'name', 'price', 'size', 'image')