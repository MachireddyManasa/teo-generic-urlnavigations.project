from django.shortcuts import render

# Create your views here.
def b1(request):
    return render(request,'b1.html')


def b2(request):
    return render(request,'b2.html')
