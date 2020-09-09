from django.urls import path

from . import views

app_name = 'stockcrash'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:stock_id>/', views.detail, name='detail'),
    path('<int:stock_id>/results/', views.results, name='results'),
    path('<int:stock_id>/view/', views.view, name='view'),
]