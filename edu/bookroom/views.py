from django.shortcuts import render,redirect
from django.contrib import messages
from .models import bookroom


# Create your views here.
def jaiho(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        room_number = request.POST['room_number']
        number = request.POST['number']
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        check_in_time = request.POST['check_in_time']
        check_out_time = request.POST['check_out_time']

        if bookroom.objects.filter(check_in_date__gte=check_in_date):
            if bookroom.objects.filter(check_in_date__gte=check_out_date):
                user= bookroom(first_name=first_name, last_name=last_name, room_number=room_number, number=number, check_in_date=check_in_date, check_out_date=check_out_date, check_in_time=check_in_time, check_out_time=check_out_time)
                user.save()
                return redirect('/')
            elif bookroom.objects.filter(check_in_date__lte=check_out_date):
                messages.info(request,'booking not possible in this date(1)')
                return redirect('jaiho')
        elif bookroom.objects.filter(check_in_date__lte=check_in_date):
            if bookroom.objects.filter(check_out_date__gte=check_in_date):
                messages.info(request,'booking not possible in this date(1)')
                return redirect('jaiho')
            else:
                user= bookroom(first_name=first_name, last_name=last_name, room_number=room_number, number=number, check_in_date=check_in_date, check_out_date=check_out_date, check_in_time=check_in_time, check_out_time=check_out_time)
                user.save()
                return redirect('/')
           
    else:
        return render(request,'bookroom.html')


                 

                     
    