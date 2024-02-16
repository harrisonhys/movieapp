from django.db import models

class MpaaRating(models.Model):
    type = models.CharField(max_length=10)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.JSONField()
    language = models.CharField(max_length=50)
    mpaaRating = models.ForeignKey(MpaaRating, on_delete=models.CASCADE)
    userRating = models.CharField(max_length=10)

    def __str__(self):
        return self.name