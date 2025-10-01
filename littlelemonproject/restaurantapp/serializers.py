from django.contrib.auth.models import User
from rest_framework import serializers
from restaurantapp.models import Menu, Booking


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Menu        
        fields = ['ID', 'Title', 'Price', 'Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['ID', 'Name', 'No_of_guests', 'BookingDate']
        # fields =  '__all__'