
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(default="../static/images/default.png")
    date = models.DateTimeField(blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
