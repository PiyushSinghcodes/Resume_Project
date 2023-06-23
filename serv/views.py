from django.shortcuts import render

# Create your views here.
def services(request):
    con={'c4':'active'}
    return render(request,'serv/services.html',con)
