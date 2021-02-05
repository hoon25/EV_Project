from django.shortcuts import render

def naverMap(request):
    print("check - sucess load map")
    return render(request, 'naverMapApi.html')

def naverMapEx1(request):
    print("check - sucess load map")
    return render(request, 'naverMapApiEx1.html')

def naverMapEx2(request):
    print("check - sucess load map")
    return render(request, 'naverMapApiEx2.html')


# Create your views here.
