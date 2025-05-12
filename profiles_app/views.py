from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HHTP methods as functions(get, post, put, patch, delete)",
            "Is similar to a traditional django view",
            "Gives you the most control over your application logic",
            "is mapped manually to urls",
        ]
        return Response({"message": "Hello!", "an_apiview": an_apiview})
