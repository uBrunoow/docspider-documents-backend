from .models import Documents
from .serializers import DocumentsSerializer, DocumentsFlatSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000
    

class DocumentsViewset(viewsets.ModelViewSet):
    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all().order_by('id')
    pagination_class = CustomPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        "is_active": ["exact"],
    }
    search_fields = ["title"]   

    @action(detail=False, methods=["get"])
    def flat(self, request):
        queryset = self.get_queryset()
        serializer = DocumentsFlatSerializer(queryset, many=True)
        return Response(serializer.data)

