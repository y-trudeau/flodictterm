from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class HelloWorld(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        """Print 'Hello, world!' as the response body."""
        content = "Hello, world!"
        return Response(content)
