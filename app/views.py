from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    return render(request,'jinjaprint.html',context={'name':'somu'})