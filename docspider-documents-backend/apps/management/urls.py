from apps.management import views as api
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"documents", api.DocumentsViewset)

urlpatterns = [
    path("", include(router.urls)),
]
