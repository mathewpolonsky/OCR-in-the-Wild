from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length = 50, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    recognized_text = models.CharField(max_length = 100, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
