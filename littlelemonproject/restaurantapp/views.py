from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, User,Booking
from .serializers import MenuSerializer, UserSerializer,BookingSerializer
from rest_framework import generics,permissions
from rest_framework.viewsets import ModelViewSet   #viewssets
from rest_framework.permissions import IsAuthenticated

class   UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet): #(viewsets.ModelViewSet)
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method in ['POST', 'PUT', 'PATCH']:
    #         return [permissions.IsAuthenticated]
        

