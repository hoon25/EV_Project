from django.shortcuts import render

# Create your views here.

def index(request):
    print('check - load index')
    return render(request, 'index.html')

def naverMapEx1(request):
    print("check - sucess load map")
    return render(request, 'naverMapApiEx1.html')

def naverMapEx2(request):
    print("check - sucess load map")
    return render(request, 'naverMapApiEx2.html')

def naverMapEx3(request):
    print("check - sucess load map")
    return render(request, 'naverMapApiEx3.html')


