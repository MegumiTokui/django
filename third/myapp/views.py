from django.shortcuts import render

# Create your views here.

posts= [{
    'title': 'aoiegh',
    'author': 'teatet',
    'date': 'dodgea',
    'age':'eibei eihw'
},
{
    'title': 'haee',
    'author': 'teeeee',
    'date': '3333',
    'age':'a3ta3t3 eihw'
},
{
    'title': 'etaetege',
    'author': 'geapog',
    'date': 'cat',
    'age':'dog het'
}]

def home(request):
    context= {
        'posts': posts
    }