from rest_framework import viewsets

from .models import Sample


class SampleView(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    authentication_class = 'authentication'
    queryset = 'queryset'

    def get_queryset(self):
        return

    def get_serializer_class(self, serializer):
        return serializer