from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Accounts.forms import UserRegisterForm
# Create your views here.


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            login(request, user)            
            return render(request, "accounts/inicio.html", {"mensaje": f'Bienvenido {user.username}'})           
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})



def register(request):
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"accounts/login.html" ,  {"mensaje":f'Usuario creado con exito'})
        else:
            return render(request,"accounts/register.html" ,  {"mensaje":f'Los datos ingresados son invalidos'})

    else:      
        form = UserRegisterForm()     

    return render(request,"accounts/register.html" ,  {"form":form})
    