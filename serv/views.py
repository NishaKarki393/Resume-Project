from django.shortcuts import render

# Create your views here.
def services(req):
    context={'services':'active'}
    return render(req,'serv/services.html',context)