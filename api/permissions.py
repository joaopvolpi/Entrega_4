
#ESSE ARQUIVO NAO ESTÁ SENDO USADO


from rest_framework.permissions import BasePermission, SAFE_METHODS
#from api.model.Evolucao import Evolucao

class IsOwnerOrReadOnly(BasePermission):
    my_safe_method = ['GET']
    mensagem = 'A evolucao deve se referir a voce para que possa ve-la'

    def has_permission(self,request,view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self,request,view,obj):
        
        if request.method in SAFE_METHODS:
            return True
        return obj.funcionario == request.user

