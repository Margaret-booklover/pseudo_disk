from django.urls import include, path
from rest_framework import routers
from google import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'folders', views.FolderViewSet)
# router.register(r'files', views.FileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# urlpatterns = [
#     path('files/', views.files_list),
#     path('files/<int:pk>/', views.file_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    path('', include('google.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
