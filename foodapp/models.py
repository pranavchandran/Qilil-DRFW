from django.db import models

# Create your models here.
class Foods(models.Model):
    def __str__(self): return self.name
    name = models.CharField(max_length=200)
    rate = models.IntegerField()
    typ = models.CharField(max_length=200, default='sweet')
    Price_range = [
        (100, '0-100'),
        (300, '100-300'),
        (500, '300-500'),
    ]
    price_range = models.IntegerField(choices=Price_range, default=100)
    image = models.ImageField(upload_to='Images/',default="Images/None/Noimg.jpg")
    # Price_range = [
    #     (100, '0-100'),
    #     (300, '100-300'),
    #     (500, '300-500'),
    # ]
    # price_range = models.CharField(max_length=2,choices=Price_range,default=100,)
