from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import generics
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

#class BookingView(APIView):
#    def get(self, request):
#        items = models.Booking.objects.all()
#        serializer = serializers.BookingSerializer(items, many=True)
#        return Response(serializer.data)

class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    
    
