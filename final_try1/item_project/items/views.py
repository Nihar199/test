from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item
from django.contrib.auth.decorators import login_required

@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()
            return redirect('items:add_item')
    else:
        form = ItemForm()
    items = Item.objects.filter(added_by=request.user)
    return render(request, 'items/add_item.html', {'form': form, 'items': items})