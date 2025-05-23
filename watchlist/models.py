from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class StreamingPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(
        to=StreamingPlatform,
        on_delete=models.CASCADE,
        related_name="watchlist",
    )
    avg_rating = models.FloatField(default=0.0)
    total_reviews = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=5),
        ]
    )
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(
        to=WatchList, on_delete=models.CASCADE, related_name="reviews"
    )
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating} | {self.watchlist.title} | {str(self.author)}"
