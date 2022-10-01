from django.shortcuts import render

# Create your views here.
def my_view(request):
    myname="Ashitha"
    myfavplayer="Dhoni"
    myfavanimal="Lion"
    myfavsub="Python"
    d={'name':myname,'player':myfavplayer,'animal':myfavanimal,'subject':myfavsub}
    return render(request,'myapp/index.html',d)