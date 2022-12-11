from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from .models import User, LotType, ParkingLot, ParkingTicket
from .forms import NewUserCreationForm, UserForm, ParkingLotForm, ParkCarForm
import datetime as dt


# login page
def loginPage(request):
    page = 'parking-login'
    if request.user.is_authenticated:
        return redirect('parking-home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User Doesn\'t Exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('parking-home')
        else:
            messages.error(request, 'Email OR Password DON\'T MATCH')

    return render(request, 'parking_login_register.html', {'page': page})


# user logout
def logoutUser(request):
    logout(request)
    return redirect('parking-home')


# home page with search
def parkingHome(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    lots = ParkingLot.objects.filter(
        Q(lot_type__name__icontains=q) |
        Q(name__icontains=q)
    )
    lot_count = lots.count()
    lot_types = LotType.objects.all()[0:5]
    parking_tickets = ParkingTicket.objects.filter(
        Q(parkingLot__lot_type__name__icontains=q))[0:5]

    context = {'lots': lots, 'lot_types': lot_types,
               'lot_count': lot_count, 'parking_tickets': parking_tickets}
    return render(request, 'parking_home.html', context)


# parking lot page
def parkinglot(request, pk):
    lot = ParkingLot.objects.get(id=pk)
    lot_tickets = lot.parkingticket_set.all()
    users = lot.users.all()

    context = {'lot': lot, 'lot_tickets': lot_tickets, 'users': users}
    return render(request, 'parkinglot.html', context)


# register user
def registerPage(request):
    form = NewUserCreationForm()

    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('parking-home')
        else:
            messages.error(request, 'An Error Occurred During Registration')
    
    print(form.errors)
    return render(request, 'parking_login_register.html', {'form': form})


# update user profile
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my-tickets', pk=user.id)

    return render(request, 'update-user.html', {'form': form})


# parking lot creation page by only admins
@login_required(login_url='parking-login')
def createParkinglot(request):
    form = ParkingLotForm()
    lot_types = LotType.objects.all()
    if request.method == 'POST':
        lot_name = request.POST.get('lot_type')
        price = request.POST.get('price')
        lot, created = LotType.objects.get_or_create(
            name=lot_name, price=price)

        ParkingLot.objects.create(
            admin=request.user,
            lot_type=lot,
            name=request.POST.get('name')
        )
        return redirect('parking-home')

    context = {'form': form, 'lot_types': lot_types}
    return render(request, 'lot_form.html', context)


# start parking page
@login_required(login_url='parking-login')
def parkCar(request):
    ticket = ParkingTicket.objects.all()
    lots = ParkingLot.objects.all()
    form = ParkCarForm()
    lot_types = LotType.objects.all()

    if request.method == 'POST':
        parking_lot = request.POST.get('parkingLot')
        pl = ParkingLot.objects.get(id=parking_lot)

        park = ParkingTicket.objects.create(
            user=request.user,
            parkingLot=pl,
            ticket=0,
            enter_time2=str(dt.datetime.now().strftime('%H:%M:%S'))
        )
        pl.users.add(request.user)
        return redirect('parking-home')

    context = {'form': form, 'lot_types': lot_types, 'lots': lots}
    return render(request, 'park.html', context)


# update parking lot information
@login_required(login_url='parking-login')
def updateParkinglot(request, pk):
    parkinglot = ParkingLot.objects.get(id=pk)
    form = ParkingLotForm(instance=parkinglot)
    lot_types = LotType.objects.all()
    if request.user != parkinglot.admin:
        return HttpResponse('Insufficient Permission')

    if request.method == 'POST':
        lot_name = request.POST.get('lot_type')
        lot = LotType.objects.get_or_create(name=lot_name)
        parkinglot.name = request.POST.get('name')
        parkinglot.lot_type.name = lot
        parkinglot.price = request.POST.get('price')
        parkinglot.save()
        return redirect('parking-home')

    context = {'form': form, 'lot_types': lot_types, 'parkinglot': parkinglot}
    return render(request, 'lot_form.html', context)


# delete parking lot
@login_required(login_url='parking-login')
def deleteParkinglot(request, pk):
    lot = ParkingLot.objects.get(id=pk)

    if request.user != lot.admin:
        return HttpResponse('Insufficient Permission')

    if request.method == 'POST':
        lot.delete()
        return redirect('parking-home')
    return render(request, 'parking-delete.html', {'lot': lot})


# browse threw parking areas
def lotTypesPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    lot_types = LotType.objects.filter(name__icontains=q)
    return render(request, 'lots.html', {'lot_types': lot_types})


# users active parking tickets
@login_required(login_url='parking-login')
def userTickets(request, pk):
    user = User.objects.get(id=pk)
    lots = user.parkinglot_set.all()
    lot_tickets = user.parkingticket_set.all()
    parking_tickets = ParkingTicket.objects.all()
    lot_types = LotType.objects.all()
    context = {
        'user': user,
        'lots': lots,
        'lot_tickets': lot_tickets,
        'parking_tickets': parking_tickets,
        'lot_types': lot_types
    }
    return render(request, 'my-tickets.html', context)


# end parking
@login_required(login_url='parking-login')
def payTicket(request, pk):
    userticket = ParkingTicket.objects.get(id=pk)
    price = userticket.parkingLot.price
    lot = userticket.parkingLot
    user = request.user

    if request.user == userticket.user:
        if request.method == 'POST':
            # userticket.enter_time = userticket.enter_time.strftime('%H:%M:%S')
            userticket.exit_time = str(dt.datetime.now().strftime('%H:%M:%S'))
            start = userticket.enter_time2
            end = userticket.exit_time
            form = '%H:%M:%S'
            total_time = (dt.datetime.strptime(end, form) -
                          dt.datetime.strptime(start, form)).seconds / 3600
            pay1 = price * 1.25
            pay2 = price * 1.5
            pay3 = price * 2
            if 0.5 >= total_time:
                userticket.ticket = total_time * price
                user.balance += userticket.ticket
                lot.users.remove(user)
                userticket.save()
                user.save()
                return redirect('my-tickets', pk=user.id)
            if 0.5 < total_time < 0.75:
                first = total_time - 0.5
                userticket.ticket = (pay1 * first) + (price * 0.5)
                user.balance += userticket.ticket
                lot.users.remove(user)
                userticket.save()
                user.save()
                return redirect('my-tickets', pk=user.id)
            if 0.75 <= total_time < 1:
                first = total_time - 0.75
                userticket.ticket = (pay2 * first) + \
                    (pay1 * 0.25) + (price * 0.5)
                user.balance += userticket.ticket
                lot.users.remove(user)
                userticket.save()
                user.save()
                return redirect('my-tickets', pk=user.id)
            if 1.0 <= total_time:
                first = total_time - 1.0
                userticket.ticket = (pay3 * first) + \
                    (pay2 * 0.25) + (pay1 * 0.25) + (price * 0.5)
                user.balance += userticket.ticket
                lot.users.remove(user)
                userticket.save()
                user.save()
                return redirect('my-tickets', pk=user.id)

    return render(request, 'ticket.html', {'obj': userticket})
