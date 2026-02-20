from django.shortcuts import render,redirect
from django.http import response
import bcrypt
from . import models

# Create your views here.
def login(request):
    
    is_user_exist = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = str(password)
        __password_bytes = password.encode(encoding="utf-8")
        
        try:
            is_user_exist = models.UserInfo.objects.get(username=f'{username}')
            if is_user_exist is not None:
                check_pw = bcrypt.checkpw(__password_bytes,is_user_exist.password_hash.encode(encoding="utf-8"))
                if check_pw:
                    request.session['user_id'] = is_user_exist.id
                    return redirect('homepage')
                else:
                    return render(request,'error.html')
            
        except models.UserInfo.DoesNotExist or Exception:
            hashed_passw = bcrypt.hashpw(__password_bytes,bcrypt.gensalt())
            models.UserInfo.objects.create(username=username,password_hash=hashed_passw.decode())
            is_user_exist = models.UserInfo.objects.get(username=username)
            request.session['user_id'] = is_user_exist.id
            return redirect('/home/homepage')
            
    return render(request, "userlogin.html")


def createuser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        password = str(password)
        __password_bytes = password.encode()
        
        try:
            is_user_exist = models.UserInfo.objects.get(username=f'{username}')
            if is_user_exist is not None:
                check_pw = bcrypt.checkpw(__password_bytes,is_user_exist.password_hash.encode(encoding="utf-8"))
                if check_pw:
                    request.session['user_id'] = is_user_exist.id
                    return redirect('/home/homepage')
                else:
                    return render(request,'error.html')
            
        except models.UserInfo.DoesNotExist or Exception:
            print('User Created')
            hashed_passw = bcrypt.hashpw(__password_bytes,bcrypt.gensalt())
            _user = models.UserInfo.objects.create(username=username,password_hash=hashed_passw.decode())
            _user.save()
            is_user_exist = models.UserInfo.objects.get(username=username)
            request.session['user_id'] = is_user_exist.id
            return redirect('homepage')
        
    return render(request,'usersignpage.html')
