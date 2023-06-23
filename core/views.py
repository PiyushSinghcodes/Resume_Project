from django.shortcuts import render

# Create your views here.
def home(request):
    con={'c':'active'}
    return render(request,'core/home.html',con)
def contact(request):
    con={'c3':'active'}
    return render(request,'core/contact.html',con)
