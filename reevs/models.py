from django.db import models
from django.contrib.auth.models import User

#Приклад: модель "кімнати"
class Rest(models.Model):
    CATEGORY_CHOICES = [
        ("econom", "Econom"),
        ("standard", "Standard"),
        ("luxe", "Luxe")
    ]
    VACATION_CHOICES = [
        ("active", "Активний"),
        ("passive", "Пасивний"),
        ("mixed", "Змішаний")
    ]

    name = models.CharField(max_length=100)  # назва місця
    tep = models.CharField(max_length=20, choices=VACATION_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='rests', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category}, {self.tep})"

    class Meta:
        verbose_name = "reevs_room"
        verbose_name_plural = "Rests"
        ordering = ["name"]


class Room(models.Model):
    rest = models.ForeignKey(Rest, on_delete=models.CASCADE, related_name="rooms")
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()# скільки людей може одночасно відпочивати
    total_rooms = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.rest.name} - {self.number} ({self.capacity})"
    
    class Meta:
        verbose_name = "rooms"
        verbose_name_plural = "rooms"

#Приклад: модель "бронювання"
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateField()
    end_time = models.DateField()
    guests_count = models.PositiveIntegerField(default=1) #
    creation_time = models.DateTimeField(auto_now_add=True) #

    def __str__(self):
        return f"{self.user.username} - {self.room.rest.name} (Room {self.room.number})"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bokings"
        ordering = ["start_time"]