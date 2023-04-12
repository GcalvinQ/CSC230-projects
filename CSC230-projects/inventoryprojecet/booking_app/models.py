from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
EQUIPMENT_CHOICES = (
    ("Desktop Computers", "Desktop Computers"),
    ("Soldering Stations", "Soldering Stations"),
    ("Electronics Station", "Electronics Stations"),
    ("Lasers", "Lasers"),
    ("3D Printers", "3D Printers"),
    ("CNC Machine", "CNC Machine"),
    ("Vacuum Former", "Vacuum Former"),
    ("Vinyl Cutter", "Vinyl Cutter"),
    ("Heat Press", "Heat Press"),
    ("Assembly Stations", "Assembly Stations"),
    ("Photo Studio", "Photo Studio"),
    ("Format Printer", "Format Printer"),
)
TIME_CHOICE = (
    ("8 AM", "8 AM"),
    ("10 AM", "10 AM"),
    ("12 AM", "12 AM"),
    ("2 PM", "2 PM"),
    ("4 PM", "4 PM"),
    ("6 PM", "6 PM"),
    ("8 PM", "8 PM"),
)
# Create your models here.
class Equipment(models.Model):
    # equipment name
    name = models.CharField(max_length=200)
    # equipment description
    description = models.TextField()
    # equipment location in makerspace
    location = models.CharField(max_length=200)
    # is the equipment dangerous
    is_dangerous = models.BooleanField(default=False)
    # equipment availability
    availability = models.BooleanField(default=True)
    # equipment image
    image = models.ImageField(upload_to='equipment_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    equipment = models.CharField(max_length=50, choices=EQUIPMENT_CHOICES, default="Desktop Computers")
    #  service = models.CharField(max_length=50, choices=EQUIPMENT_CHOICES, default="Desktop Computers")
    day = models.DateField(default=datetime.now)
    #### USER SPECIFIED TIMES ####
    #start_time = models.TimeField()
    #end_time = models.TimeField()
    ##### ADMIN SPECIFIED TIMES #####
    time = models.CharField(max_length=10, choices=TIME_CHOICE, default="2 PM")
    booked_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.user.username} | booked {self.equipment[0]} | day: {self.day} | time: {self.time}"