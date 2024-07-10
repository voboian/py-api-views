from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.rows} rows x {self.seats_in_row} cols)"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    cinema_halls = models.ManyToManyField(CinemaHall)

    def __str__(self):
        return self.title
