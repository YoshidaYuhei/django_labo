from rest_framework import viewsets
from rest_framework.response import Response
from airp.infra.query.citation import CitationQuery

class CitationsViewSet(viewsets.ViewSet):
    def list(self, request):
        query = CitationQuery()
        data = query.all()
        return Response(data)

    def detail(self, request):
        query = CitationQuery()
        data = query.pick(request.id)
        return Response(data)

    # def search(self, request):
    #     query = CitationQuery()
    #     return query.search(request)

    def update(self, request, pk=None):
        return Response({'message': 'Hello, world!'})

    def partial_update(self, request, pk=None):
        return Response({'message': 'Hello, world!'})

    def destroy(self, request, pk=None):
        return Response({'message': 'Hello, world!'})