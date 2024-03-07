from rest_framework import viewsets
from rest_framework.response import Response

class CitationViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'Hello, world!'})

    def retrieve(self, request, pk=None):
        return Response({'message': 'Hello, world!'})

    def create(self, request):
        return Response({'message': 'Hello, world!'})

    def update(self, request, pk=None):
        return Response({'message': 'Hello, world!'})

    def partial_update(self, request, pk=None):
        return Response({'message': 'Hello, world!'})

    def destroy(self, request, pk=None):
        return Response({'message': 'Hello, world!'})