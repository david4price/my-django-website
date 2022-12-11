from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, ParkingLot, ParkingTicket


class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email', 'car_num', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields= ['name', 'email', 'car_num']


class ParkingLotForm(ModelForm):
    class Meta:
        model = ParkingLot
        fields = '__all__'
        exclude = ['admin', 'users']


class ParkCarForm(ModelForm):
    class Meta:
        model = ParkingTicket
        fields = '__all__'
