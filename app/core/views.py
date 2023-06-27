from rest_framework import viewsets

from .models import Sample


class SampleView(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
