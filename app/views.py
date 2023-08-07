from django.shortcuts import render,HttpResponse,redirect
from .models import Book

# Create your views here.

def welcome_page(request):
    return render(request,'welcome.html')

def show_all_books(request):
    books =Book.objects.all()
    return render(request,'showbooks.html',{'allbooks':books})

def show_single_book(request,id):
    book_obj = Book.objects.get(id=id)
    return render(request,'bookdetail.html',context={"book":book_obj})

def add_single_book(request):
    if request.method== 'POST':
        print("in post method")
    elif request.method=='GET':
        return render(request,'addbook.html')

def edit_single_book(request,id):
    book_obj=Book.objects.get(id=id)
    return render(request,'bookedit.html',{'single_book':book_obj})


def delete_single_book(request):
    book_obj=Book.objects.get(id=id)
    return render(request,'deletebook.html',{'single_book':book_obj})


# ------fo-r- fo-rms-------------------

from .forms import GeeksForm,BookForm,AddressForm
def form_view(request):
    if request.method == "POST":
        data=request.POST
        form= BookForm(data)
        if form.is_valid():
            # print("in if condition")
            form.save()
            return redirect("show_books")
        print(data)
        return HttpResponse("okkk")
    elif request.method =="GET":
    # context = {}
    # print(GeeksForm())
    # context['form']=GeeksForm
        return render(request,'book_form_test.html',{"bookform":BookForm()})

def viewx(request):
    return HttpResponse("hello")