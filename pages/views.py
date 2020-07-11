import os
import smtplib
from email.message import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from pages.models import Furniture
from .sms import notify_admin
def index(request):
    template_name = 'pages/index.html'
    return render(request, template_name)

def funitures_list(request):
    template_name = 'pages/category.html'
    return render(request, template_name)

def about(request):
    pass

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        #SENDINg MAIL
        MAIL_USERNAME = os.environ.get('AMD_MAIL_USERNAME')
        EMAIL_PASS = os.environ.get('AMD_EMAIL_PASS')

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = MAIL_USERNAME
        #Start the Context Manager to automatically manage the server Conncetion
        msg.set_content("Message from Site")
        msg.add_alternative(f"""\
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <title>Inquiry From AMDIGITAL FURNITURE</title>
            </head>
            <body>
                <div class="container">
                    <div class="row">
                        <div class="col">
                            { message } from: {email}
                        </div>
                    </div>
                </div>
                
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>  
            </body>
            </html>
        """, subtype="html")
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
                #Since we have identified ourselves as secure connection we can now login
                smtp.login(MAIL_USERNAME, EMAIL_PASS)
                #Send Mail
                smtp.send_message(msg)
            print ("--Email Success--")
            messages.success(request, "Your Messages have sent successfully! We will get back to you soon")
            phone = "+254718686209"
            notify_sms = f"You have a mail from {name}, Please open Mail to view it at AMDFurnitures"
            notify_admin(phone, notify_sms)
            return redirect('furn-home')
        except ConnectionRefusedError:
            print("Please try Again...Email Unsuccessful")
            messages.danger(request, "Something went wrong, Please Try again")
            return redirect('contact')

    else:
        template_name = 'pages/contact.html'
        return render(request, template_name)
#Home_View
class HomeListView(ListView):
    model = Furniture
    template_name='pages/furn_home.html'
    context_object_name = 'furnitures'
#LISTVIEW
class FurnitureListView(ListView):
    model = Furniture
    template_name = 'pages/furnitures.html'
    context_object_name = 'furnitures'

class FurnitureDetailView(DetailView):
    model = Furniture 
    template_name = 'pages/furniture_single.html'
    context_object_name = 'furniture'
