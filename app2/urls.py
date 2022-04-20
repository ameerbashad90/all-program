from app2.views import a2_rohit
from django.urls import path
app_name='app2'
urlpatterns=[
    path('a2_rohit/',a2_rohit,name='a2_rohit'),
]