from django.urls import path, include
from blog.api.api_views import BlogViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', BlogViewSet)

urlpatterns = [
    path('blogs/', include(router.urls))
    # path('posts/', post_list_api),
    # path('posts/<int:pk>', post_detail_api),

]
