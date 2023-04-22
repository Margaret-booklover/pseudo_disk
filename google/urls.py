from django.urls import path, include
from rest_framework.routers import DefaultRouter
from google import views

router = DefaultRouter()
router.register(r'folders', views.FolderViewSet, basename="folders")
router.register(r'files', views.FileViewSet, basename="files")
router.register(r'users', views.UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
    #path('uploads/', views.show_file),
]
