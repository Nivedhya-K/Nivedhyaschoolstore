from .import views
from django.urls import path
urlpatterns = [
    path('',views.home,name="home"),
    path('register', views.register, name="register"),
    path('login',views.login,name="login"),
    path('form',views.form,name="form"),
    path('submit_form',views.submit_form,name="submit_form"),
    path('logout',views.logout,name="logout"),

]