from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name='register'),
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name= "room"),
    path("profile/<str:pk>/", views.profile, name="user-profile"),
    path("create-room/", views.CreateRoom, name= "create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name= "update-room"),
    path("delete-room/<str:pk>/", views.deleteRoom, name= "delete-room"),
    path("delete-message/<str:pk>/", views.deleteMessages, name ="delete-message"),
    path("update-user/", views.UpdateUser, name='update-user'),
    path("topics/", views.topicsPage, name='topics'),
    path("activity/", views.activityPage, name="activity"),
]
