from django.shortcuts import render,redirect
from userlogin import models
# Create your views here.

def homepage(request):
    # use Django shortcut to render the template and ensure request is used
    if "user_id" not in request.session:
        return redirect('')
    
    return render(request, 'homepage.html')

def about(request):
    if "user_id" not in request.session:
        return redirect('')
    return render(request,'aboutpage.html')