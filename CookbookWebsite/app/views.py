
from django.shortcuts import render
 
from .models import recipeList
 
def home(request):
    db = recipeList.objects.all()
    return render(request,'app/index.html', {"db":  recipeList})

def Add(request):
    db = recipeList.objects.all()
    return render(request,'app/addrecipe.html', {"db": recipeList})

def Random(request):
    db = recipeList.objects.all()
    return render(request,'app/random.html', {"db": recipeList})

def List(request):
    db = recipeList.objects.all()
    return render(request,'app/list.html', {"db": recipeList})