from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import Cake

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=User
        fields=["id","email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Cake
        fields="__all__"

    