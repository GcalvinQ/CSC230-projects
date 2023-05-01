from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages


# Create your views here.

import os
import csv
import hashlib

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        hashed_email = hashlib.sha256(email.encode()).hexdigest()

        # Get the absolute path to the CSV file
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(BASE_DIR, 'data', 'CS-majors-minors.csv')

        # Check if the email exists in the CSV file
        form = None
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Spartans Email Address'] == hashed_email:
                    # If the email exists, create the user and redirect to the login page
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                        user = form.save()
                        return redirect('user-login')
            # If the email doesn't exist, display an error message
            if form is None:
              return redirect('user-registerfail')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


def registerFail(request):
    return render(request, 'user/registerfail.html')

def profile(request):
    context = {

    }
    return render(request, 'user/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('userPanel')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)


# views.py

from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View



class ContactAdminView(View):
    template_name = 'contact_admin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        # Get the message and subject from the POST data
        message = request.POST.get('message')
        subject = request.POST.get('subject')

        # Get the admin email addresses from the settings file
        admin_emails = ['umang.ggrg@gmail.com', 'fak.brodi@gmail.com']

        # Get the user's email address from the request object
        user_email = request.user.email

        # Send the email to the admin email addresses
        send_mail(
            subject,
            message,
            user_email,
            admin_emails,
            fail_silently=False,
        )

        # Render a success message to the user
        return render(request, self.template_name, {'success': True})

from django.views.generic import View
from django.http import JsonResponse
from datetime import datetime, time

class UpdateWebsiteStatusView(View):
    def post(self, request):
        now = datetime.now().time()
        if now >= time(9, 0) and now <= time(17, 0):
            WebsiteStatus.objects.update(active=True)
        else:
            WebsiteStatus.objects.update(active=False)
        return JsonResponse({'status': 'ok'})


