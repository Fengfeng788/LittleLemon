from django.db import models

# Create your models here.
class  User(models.Model):
    ID = models.IntegerField(primary_key=True,max_length=11)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Password = models.CharField(max_length=255)
    # Phone = models.CharField(max_length=15)
    # Address = models.CharField(max_length=255)
    # City = models.CharField(max_length=255)
    # State = models.CharField(max_length=255)
    # Zipcode = models.CharField(max_length=10)
    # Created_at = models.DateTimeField(auto_now_add=True)
    # Updated_at = models.DateTimeField(auto_now=True)


class Menu(models.Model): 
    ID = models.IntegerField(primary_key=True,max_length=5)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField(max_length=5)
 
    def get_item(self):
        return f'{self.Title}: {str(self.Price)}'

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
    # def __str__(self):
    #     return self.Title
    
class  Booking(models.Model):
    ID = models.IntegerField(primary_key=True,max_length=11)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateField()
    # Menu = models.ForeignKey(Menu, on_delete=models.CASCADE)