from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from api.model.Postagem import Postagem
from api.model.Evolucao import Evolucao

from django.shortcuts import get_object_or_404

from .permissions import IsOwnerOrReadOnly

from .serializers import PostagemSerializer, UserSerializer, EvolucaoSerializer
from rest_framework import generics, status, viewsets
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied

from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser


class EvolucaoViewSet(viewsets.ModelViewSet):
    queryset = Evolucao.objects.all()
    serializer_class = EvolucaoSerializer

    permission_classes = [IsAdminUser] #SOMENTE O ADMIN PODE POSTAR EVOLUCAO DOS FUNCIONARIOS


'''
class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer


    permission_classes = [IsAdminUser, IsAuthenticated] #SOMENTE O ADMIN PODE POSTAR METAS
    
    def destroy(self, request, *args, **kwargs):
        postagem = Postagem.objects.get(pk=self.kwargs["pk"])
        if not request.user == postagem.created_by:
            raise PermissionDenied("Você não pode deletar essa postagem")
            return super().destroy(request, *args, **kwargs)

'''

class PostagemList(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        postagem = Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data
        print(request.data)
        return Response(data)

    def post(self, request):
        nome = request.data['nome']
        descricao = request.data['descricao']       
        postagem = Postagem(nome= nome, descricao=descricao)
        postagem.save()
        data = PostagemSerializer(postagem).data

        permission_classes = [IsAdminUser] #SOMENTE O ADMIN PODE POSTAR METAS, MAS NAO ESTA FUNCIONANDOOO
        
        return Response(data)

class PostagemDetail(APIView):
    def delete(self,request,pk):
        post = get_object_or_404(Postagem, pk=pk)
        post.delete()

        data = PostagemSerializer(post).data

        return Response(data)



class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
        permission_classes = ()
        def post(self, request):
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                return Response({"token": user.auth_token.key}) #RETORNA UM TOKEN
            else:
                return Response({"error": "Senha Incorreta"}, status=status.HTTP_400_BAD_REQUEST)  

