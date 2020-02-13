from django.urls import path, include
from users.api.api_views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('users/', include(router.urls))
    # path('posts/', post_list_api),
    # path('posts/<int:pk>', post_detail_api),

]
