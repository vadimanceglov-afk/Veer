from django.db import models
from django.contrib.auth.models import User

#Приклад: модель "кімнати"
class Room(models.Model):
    CATEGORY_CHOICES = [
        ("econom", "Econom"),
        ("standard", "Standard"),
        ("luxe", "Luxe")
    ]
    number = models.IntegerField()
    capacity = models.IntegerField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='rooms')

    def __str__(self):
        return f"Room №{self.number} for {self.capacity} person(s)"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]

#Приклад: модель "бронювання"
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room}"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bokings"
        ordering = ["start_time"]