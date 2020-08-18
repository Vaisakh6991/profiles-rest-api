from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """ Test API View  """

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