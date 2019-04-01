from django.shortcuts import render
from . models import Contact
import requests
import json

# Create your views here.
def home(request):
    if request.method =='POST':
        firstname= request.POST.get('fname')
        lastname = request.POST.get('lname')

        anything=requests.get('http://api.icndb.com/jokes/random?firstName=' +firstname +'&amp;lastName=' + lastname)
        json_data=json.loads(anything.text)

        joke=json_data.get('value').get('joke')

        context={
            'joker': joke
        }

        return render(request,'myapp/home.html', context)

    else:
        firstname="Megumi"
        lastname="Tokui"
        anything=requests.get('http://api.icndb.com/jokes/random?firstName=' +firstname +'&amp;lastName=' + lastname)
        json_data=json.loads(anything.text)

        joke=json_data.get('value').get('joke')

        context={
            'joker': joke
        }
        return render(request, 'myapp/home.html', context)
       



def portfolio(request):
    return render(request, 'myapp/portfolio.html')

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r,message=message_r)
        c.save()

        return render(request, 'myapp/thank.html')

    else:
        return render(request, 'myapp/contact.html')
