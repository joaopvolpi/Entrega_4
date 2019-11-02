#PASSAR DE PYTHON PARA JSON

from rest_framework import serializers
from api.model.Postagem import Postagem
from api.model.Evolucao import Evolucao
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class EvolucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolucao
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'
        