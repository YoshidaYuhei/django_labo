from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from airp.infra.query.citation import CitationQuery
from airp.domain.services.citation import CitationService
from airp.domain.serializers.citation import CitationCreateIn

class CitationsViewSet(APIView):
    # permission_classes = [IsAuthenticated]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query = CitationQuery()
        self.service = CitationService()

    def list(self, request):
        data = self.query.all()
        return Response(data)

    def detail(self, request):
        data = self.query.pick(request.id)
        return Response(data)

    # def search(self, request):
    #     query = CitationQuery()
    #     return query.search(request)

    def create(self, request):
        ser = CitationCreateIn(data=request.data)
        if ser.is_valid():
            validated_data = ser.validated_data
            self.service.create(ser)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=400) 

    def partial_update(self, request, pk=None):
        return Response({'message': 'Hello, world!'})

    def destroy(self, request, pk=None):
        return Response({'message': 'Hello, world!'})