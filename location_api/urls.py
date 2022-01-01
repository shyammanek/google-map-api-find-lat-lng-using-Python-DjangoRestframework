from django.urls import path
from . import views
urlpatterns = [
    path('getmp/<str:getAddressDetails>/<str:flag>/',views.get_lat_lng),
]