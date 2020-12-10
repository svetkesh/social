"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
# from .views import UserList, UserDetail, PostList, PostDetail

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
# ]

from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    UserViewSet, PostViewSet, LikeViewSet, DislikeViewSet
)

router = SimpleRouter()

router.register('likes', LikeViewSet, basename='likes')
router.register('dislikes', DislikeViewSet, basename='dislikes')

# router.register('users', UserViewSet, base_name='users')
router.register('users', UserViewSet, basename='users')
# router.register('', PostViewSet, base_name='posts')

router.register('posts', PostViewSet, basename='posts')
router.register('', PostViewSet, basename='posts')



urlpatterns = router.urls
