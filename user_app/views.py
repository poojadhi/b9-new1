from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.

def user_register(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = NewUserForm()
        return render(request,"register.html",context={"register_form":form})
    
