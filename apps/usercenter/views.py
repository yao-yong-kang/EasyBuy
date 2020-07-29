from django.shortcuts import render, redirect

# Create your views here.
def memberIndex(request):
    return render(request, 'usercenter/Member.html')