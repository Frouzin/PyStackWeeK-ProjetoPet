from django.shortcuts import render

def listar_pets(request):
    if request.method == "GET":
        return render(request, 'listar_pets.html')
        
# Create your views here.
