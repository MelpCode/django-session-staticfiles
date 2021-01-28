from django.shortcuts import render,redirect
from django.contrib import messages

def login(request):
    
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            request.session['first_name'] = email
            return redirect('/index')
        return redirect('/login')

    return render(request,'login.html')

def index(request):
    sesion = request.session.get('first_name')
    if sesion:
        return render(request,'index.html',{"sesion":sesion})
    else:
        messages.add_message(request,messages.ERROR,'Inicie Sesión para acceder ...')
        return redirect('/login')
        
def logout(request):
    
    del request.session['first_name']
    messages.add_message(request,messages.SUCCESS,'Cerro Sesión correctamente')
    return redirect('/login')