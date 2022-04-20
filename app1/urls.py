from app1.views import a1_virat
from django.urls import path
app_name='app1'
urlpatterns=[
    path('a1_virat/',a1_virat,name='a1_virat'),
]