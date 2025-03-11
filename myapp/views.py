from django.shortcuts import render ,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"Shruti is Smart",
        "variable2":"Shreya is Mad"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home Page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is Services Page')

def contact(request):
    if request.method=="POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        desc=request.POST.get('desc') 

        if not desc:
            print("Description field is missing or empty!")

        contact=Contact(name=name,email=email,phone=phone,desc=desc,
                        date=datetime.today())
        contact.save()
        messages.success(request, "Submitted Succesfully!")
    return render(request, 'contact.html')
    # return HttpResponse('This is Contact Page')