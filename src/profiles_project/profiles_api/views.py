from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """ Test API View  """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of APIView features """

        an_apiview = [
            'Uses Http Methods as function (get, post, patch, put, delete)',
            'It similar to a traditional Django view',
            'Gives you the most control over your logic',
            'It mapped manually to URLs'
        ]

        # A Response object must pass a dictionary to return a dictionary
        return Response({'message': 'Hello','an_apiview': an_apiview})
    
    def post(self, request):
        """ Creae hello message with our name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating a Specific Object """

        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Updates only the fields provided in the request """

        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """ Deletes an Object """

        return Response({'method': 'DELETE'})