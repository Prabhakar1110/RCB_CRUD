from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Player(models.Model):
    ROLE_CHOICES = [
        ("Batsman", "Batsman"),
        ("Bowler", "Bowler"),
        ("All Rounder", "All Rounder"),
        ("Wicket Keeper", "Wicket Keeper"),
    ]
    COUNTRY_CHOICES = [
        ("India", "India"),
        ("Australia", "Australia"),
        ("England", "England"),
        ("South Africa", "South Africa"),
        ("Bangladesh", "Bangladesh"),
        ("Sri Lanka", "Sri Lanka"),
        ("NewZeland", "NewZeland"),
        ("WestIndies", "WestIndies"),
        ("Other","Other"),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    profile_pic = models.ImageField(upload_to="player/")
    is_captain = models.BooleanField(default=False)
    fav_food = models.ManyToManyField(Food)
    
    def __str__(self):
        return f"{self.name} - {self.role}"
