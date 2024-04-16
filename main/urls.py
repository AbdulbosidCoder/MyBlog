from .views import *
from .drf_yasg import urlpatterns as doc_url
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'project', viewset=ProjectViewSet, basename='project')
router.register(r'user', basename='user', viewset=PostViewSet)
router.register(r'send_telegram', viewset=CommentViewSet, basename='send_telegram')

urlpatterns = [
    path(r'', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += doc_url
