from django.shortcuts import render

# Create your views here.


posts=[
    {
        'author':'Lohit',
        'title':'New Book',
        'content': 'This iS very nice book',
        'date': 'July 20, 2019'
    },
    {
        'author':'Megumi',
        'title':'New Book 2',
        'content': 'This iS very nice book  well somethuing',
        'date': 'July 20, 2029'
    }
]

def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'newblog/home.html', context)


def about(request):
    return render(request, 'newblog/about.html')


def contact(request):
    return render(request, 'newblog/contact.html')