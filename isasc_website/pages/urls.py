from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', index1, name='index1'),
    path('our_story/', our_story, name='our_story'),
    path('about_us/', about_us, name='about_us'),
    path('team/', team, name='team'),
]