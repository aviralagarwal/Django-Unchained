
from django.contrib import admin

from .models import Stock
from .models import StockInfo

admin.site.register(Stock)
admin.site.register(StockInfo)