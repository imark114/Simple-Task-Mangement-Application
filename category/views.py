from django.shortcuts import render, redirect
from .forms import AddCategory
# Create your views here.

def addCategory(request):
    if request.method == 'POST':
        category_form = AddCategory(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    category_form = AddCategory()
    return render(request,'add_category.html', {'form': category_form})