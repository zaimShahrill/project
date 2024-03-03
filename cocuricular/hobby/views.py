from django.shortcuts import render
from hobby.models import Hobbies

# Create your views here.

# Create your views here.
def index(request):
    return render(request,'index.html')

def u_hobby(request):
    if request.method == 'POST':
        name = request.POST['name']
        hobby= request.POST['hobby']
        gender= request.POST['gender']
        data = Hobbies(name=name,hobby=hobby, gender=gender)
        data.save()

    data=Hobbies.objects.all()
    dict = {
        'allreview': data
    }
    return render(request,'u_hobby.html',dict)