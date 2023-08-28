from django.db import models


class Track(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    duration = models.FloatField()
    last_play = models.DateTimeField()

    def __str__(self):
        return self.title
