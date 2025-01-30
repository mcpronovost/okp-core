from rest_framework.views import APIView
from rest_framework.response import Response


class MeView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
