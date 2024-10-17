from .models import CarList
from .serializers import CarSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

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
    

    
    def post(self, request, format=None):
        """
        Create a task.
        """
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CarDetail(APIView):
    """
    Returns a single car and allows updates and deletion of a car.
    """
    def get_object(self, car_id):
        try:
            return CarList.objects.get(pk=car_id)
        except CarList.DoesNotExist:
            raise Http404

    def get(self, request, car_id, format=None):
        car = self.get_object(car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, car_id, format=None):
        car = self.get_object(car_id)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, car_id, format=None):
        car = self.get_object(car_id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)