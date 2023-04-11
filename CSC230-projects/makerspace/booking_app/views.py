from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    ''' ONLY RENDER THE LANDING TEMPLATE '''
    return render(request, "index copy.html", {})

def booking(request):
    ''''''
    # Calling 'validWeekday' function to Loop days you want in the next 21 days
    weekdays = validWeekday(22)
    # Only sow the days that are not full
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == "POST":
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please Make A Equipment Selection.")
            return redirect('booking')
        
        # store the day and equipment in django session
        request.session['day'] = day
        request.session['service'] = service

        return redirect('bookingSubmit')
    
    equipment = Equipment.objects.all()
    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'equipment': equipment,
    })

def bookingSubmit(request):
    ''' Get session data (equipment, day) then checks which time of the selected date
        is not booked. When the user selects their time it gets stored in the database. 
     '''
    user = request.user
    times = ["8 AM","10 AM","12 AM","2 PM","4 PM","6 PM","8 PM"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Get stored data from django session
    day = request.session.get('day')
    # Get equipment object based on the value submitted in the form
    equipment = request.session.get('service')

    # Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if equipment != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == "Tuesday" or date =="Wednesday" or date=="Thursday" or date=="Friday":
                    if Schedule.objects.filter(day=day).count() < 11:
                        if Schedule.objects.filter(day=day, time=time).count() < 1:
                            AppointmentForm = Schedule.objects.get_or_create(
                                user = user,
                                equipment = equipment,
                                day = day,
                                time = time,
                            )
                            messages.success(request, "Appointment Saved.")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved.")
                    else:
                        messages.success(request, "The Selected Day Is Full.")
                else: 
                    messages.success(request, "The Selected Date Is Incorrect.")
            else: 
                messages.success(request, "The Selected Date Isn't In The Correct Time Period.")
        else: 
            messages.success(request, "Please Select A Equipment.")
    return render(request, 'bookingSubmit.html', {
        'times':hour,
    })

def userPanel(request):
    ''' Show the user's booked appointments and allow users to edit appointments '''
    user = request.user
    appointments = Schedule.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user':user,
        'appointments': appointments,
    })

def userUpdate(request, id):
    '''  
        Take the id argument from the appointment selected to edit/update appointment
        listings
    '''
    appointment = Schedule.objects.get(pk=id)
    userdatepicked = appointment.day
    # Copy Booking
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    # calling 'validWeekday' function to loop  you want in the next 21 days
    weekdays = validWeekday(22)

    # Only show the days that are not full
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', id=id)
    
    return render(request, 'userUpdate.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'delta24': delta24,
        'id': id,
    })

def userUpdateSubmit(request, id):
    '''
    Save or Update the appointment data
    '''
    user = request.user
    times = ["8 AM","10 AM","12 AM","2 PM","4 PM","6 PM","8 PM"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')

    # Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, id)
    appointment = Schedule.objects.get(pk=id)
    userSelectedTime = f"{appointment.start_time} - {appointment.end_time}"
    if request.method == "POST":
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == "Monday" or date == "Tuesday" or day == "Wednesday" or date == "Thursday" or date == "Friday":
                    if Schedule.objects.filter(day=day).count() < 11:
                        if Schedule.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            AppointmentForm = Schedule.objects.filter(pk=id).update(
                                user = user,
                                service = service,
                                day = day,
                                time = time,
                            )
                            messages.success(request, "Appointment Edited.")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before.")
                    else:
                        messages.success(request, "The Selected Day Is Full.")
                else:
                    messages.success(request, "The Selected Date Is Incorrect.")
            else: 
                messages.success(request, "The Selected Date Isn't In The Correct Time Format.")
        else:
            messages.success(request, "Please Select A Equipment.")
        return redirect("userPanel")
    
    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id':id,
    })

def staffPanel(request):
    ''' 
    Shows the bookings for the next 21 days in the template 
    -- For Administrators Only --
    '''
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Schedule.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'staffPanel.html', {
        'items':items,
    })

def dayToWeekday(x):
    '''
    Takes an argument x (day) and converts it to a string to show user
    '''
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    '''
    Takes an argument (days) and checks if each day in the period is 
    Monday, Wednesday, or Saturday
    '''
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y=="Thursday" or y=="Friday":
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays

def isWeekdayValid(x):
    '''
    Takes a argument "x" and checks the list of days from validWeekdays()
    if the days are full or not. Then returns a list of weekdays on Monday, Wednesday, Saturday,
    of times that are not completely booked
    '''
    validateWeekdays = []
    for j in x:
        if Schedule.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    '''
    Takes two arguments (times, day) to check which times of the day
    are free to be booked by the user
    '''
    # Only show the time of day that has not been selected
    x = []
    for k in times:
        if Schedule.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    '''
    Display the appointment that the user wants to edit
    '''
    # ONly show the time of day that has not been selected before
    x = []
    appointment = Schedule.objects.get(pk=id)
    time = appointment.end_time
    for k in times:
        if Schedule.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x

def equipmentPage(request):
    equipment = Equipment.objects.all()
    context = {'equipment': equipment}
    return render(request, 'equipment.html', context)
