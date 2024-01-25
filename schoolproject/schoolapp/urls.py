from .import views
from django.urls import path
app_name='schoolapp'
urlpatterns = [
    path('',views.home,name="home"),
]