from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.registerPage, name='parking-register'),
    path('login/', views.loginPage, name="parking-login"),
    path('logout/', views.logoutUser, name="parking-logout"),

    path('', views.parkingHome, name="parking-home"),
    path('parking-lot/<str:pk>/', views.parkinglot, name="parking-lot"),
    path('park-car/', views.parkCar, name="park-car"),
    path('my-tickets/<str:pk>/', views.userTickets, name="my-tickets"),
    path('pay-ticket/<str:pk>/', views.payTicket, name="pay-ticket"),

    path('create-parking-lot/', views.createParkinglot, name="create-parking-lot"),
    path('update-lot/<str:pk>/', views.updateParkinglot, name="update-lot"),
    path('delete-parking-lot/<str:pk>/', views.deleteParkinglot, name="delete-parking-lot"),

    path('parking-areas/', views.lotTypesPage, name="parking-areas"),

    path('update-user/', views.updateUser, name="update-user"),
]