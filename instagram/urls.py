from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activate/<str:uidb64>/<str:token>/',views.activate, name='activate'),
    path('logout/', views.logout_view, name='logout')

]


