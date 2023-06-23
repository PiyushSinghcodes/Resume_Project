from django.shortcuts import render

# Create your views here.
def skills(request):
    con={'c2':'active'}
    return render(request, "edu/s.html",con)
