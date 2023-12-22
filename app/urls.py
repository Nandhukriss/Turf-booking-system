from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('booking',views.booking,name='booking'),
    
]