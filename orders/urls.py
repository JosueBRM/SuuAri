from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    
]
