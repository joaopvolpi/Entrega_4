from django.urls import path 
from rest_framework.routers import DefaultRouter
from api.views import EvolucaoViewSet, PostagemList,PostagemDetail, UserCreate, LoginView #,PostagemViewSet

router = DefaultRouter()
#router.register('postagem', PostagemViewSet, base_name='postagem')
router.register('evolucao', EvolucaoViewSet, base_name='evolucao')



urlpatterns = [
    path('postagem/', PostagemList.as_view()),
    path('postagem/<int:pk>', PostagemDetail.as_view()),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]
urlpatterns+=router.urls


