from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('activate/<str:uidb64>/<str:token>/',views.activate, name='activate'),
    path('profile/', views.profile, name='create-profile'),
    path('profile/<int:id>', views.profile_user, name='dipslay-profile'),
    path('post/image/',views.post_image,name='post-image'),
    path('logout/', views.logout_view, name='logout')

]


