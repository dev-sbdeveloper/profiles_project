from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_app import serializers
from profiles_app import models
from profiles_app import permissions


class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HHTP methods as functions(get, post, put, patch, delete)",
            "Is similar to a traditional django view",
            "Gives you the most control over your application logic",
            "is mapped manually to urls",
        ]
        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = "Hello {}!".format(name)
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "Uses actions(list, create, retrieve, update, partial_update, destroy)",
            "Automatically maps to urls using routers",
            "Provides more functionality with less code",
        ]
        return Response({"message": "Hello", "a_viewset": a_viewset})

    def create(self, request):
        """Handle creating an object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = "Hello {}!".format(name)
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles retrieving an object"""
        return Response({"Method": "GET"})

    def update(self, request, pk=None):
        """Handles updating an object"""
        return Response({"Method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""
        return Response({"Method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handles deleting an object"""
        return Response({"Method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "email",
        "name",
    )


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
