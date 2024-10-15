from .models import CarList
from .serializers import CarSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class CarListView(APIView):
    """
    View all tasks.
    """
    def get(self, request, format=None):
        """
        Return a list of all tasks.
        """
        cars = CarList.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)