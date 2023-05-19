from django.shortcuts import render
from apply.forms import applyform
from apply.models import application
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives

# Create your views here.
def thank(request):
    return render(request, 'thank.html')

def applications(request):
    if(request.method=="POST"):
        first_name = request.POST["t"]
        Last_name = request.POST["a"]
        place = request.POST["b"]
        age = request.POST["p"]
        email_field = request.POST["q"]
        user = application.objects.create(first_name=first_name,last_name=Last_name,place=place,age=age,email_field=email_field)
        user.save()
        subject = "Thank you"
        message = f'Thank you for registering {user.first_name}'
        from_mail = settings.EMAIL_HOST_USER
        recipient_list = [user.email_field]
        msg=EmailMultiAlternatives(subject, message, from_mail, recipient_list)
        msg.content_subtype='html'
        msg.send()
        return thank(request)
    return render(request,'application.html')

