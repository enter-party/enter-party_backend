from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from . import views
from .views import MyView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('test/', MyView.as_view()),
    path('user/', include('user.urls')),
    path('', include('authentication.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = [path('api/', include((urlpatterns)))]

