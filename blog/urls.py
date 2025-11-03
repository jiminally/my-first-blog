from django.urls import path, include
from . import views
from rest_framework import routers

# REST API 라우터 설정
router = routers.DefaultRouter()
router.register('Post', views.blogImage)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api_root/', include(router.urls)),  # API 엔드포인트
]