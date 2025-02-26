from django.shortcuts import render, get_object_or_404, redirect
from  .models import Member
# Create your views here.

def index(request):
    enjoy = Member.objects.all()
    return render(request, 'app.html', {'enjoy': enjoy})


def add(request):
    return render(request, 'add.html')


def add_record(request):
#IMPORTANT PARTS
    x = request.POST['first']
    y = request.POST['last']
    f = request.POST['country']
    
    enjoy = Member(firstname=x, lastname= y,country= f)
    
    enjoy.save()
    return redirect("/")

def delete(request, id):
    enjoy = Member.objects.get(id = id)
    enjoy.delete() 
    return redirect("/")


def updating(request, id):
    enjoy = Member.objects.get(id = id)
    return render(request, 'app.html', {'enjoy': enjoy})
    
def upRec(request, id):
    enjoy = get_object_or_404(Member, id=id)
    
    if request.method == 'POST':
        x = request.POST.get('first')
        y = request.POST.get('last')
        f = request.POST.get('country')

        
        
        enjoy.firstname = x
        enjoy.lastname = y
        enjoy.country = f
        enjoy.save()
    
        return redirect("/")
    return render(request, 'updating.html', {'enjoy': enjoy})


   