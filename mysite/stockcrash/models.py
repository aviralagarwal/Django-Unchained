from django.db import models
from django.utils import timezone
import datetime

class Stock(models.Model):
    stock_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.stock_name




class StockInfo(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    stock_info = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.stock_info