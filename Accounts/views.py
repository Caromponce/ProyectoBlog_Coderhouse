from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from Accounts.forms import UserRegisterForm, UserEditForm, changePasswordForm
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

def logout_request(request):
    logout(request)
    return redirect("/")

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
    
def profile(request):
    return render(request, 'accounts/profile.html')



def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            return render(request, "app/home.html")
        
    else:
        form = UserEditForm(instance = request.user)
    return render(request, "accounts/editProfile.html", {"form": form, "usuario": user})


def change_password(request):
    if request.method == 'POST':
        form = changePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('/accounts/profile')
    else:
        form = changePasswordForm(user=request.user)

    return render(request, 'accounts/changePassword.html', { 'changePasswordForm' : form })