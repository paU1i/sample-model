from django.shortcuts import render, redirect

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Imports the Item class
from todolist2.models import Item


# Action for the default /todolist2/ route.
@login_required
def home_action(request):
    if not request.user.email.endswith("@andrew.cmu.edu"):
        return render(request, 'todolist2/unauthorized.html')

    return render(request, 'todolist2/index.html', {'items': Item.objects.all()})


# Action for the /todolist2/add-item route.
@login_required
def add_action(request):
    if not request.user.email.endswith("@andrew.cmu.edu"):
        return render(request, 'todolist2/unauthorized.html')

    # Set context with current list of items so we can easily return if we discover errors.
    context = { 'items': Item.objects.all() }

    # Adds the new item to the database if the request parameter is present
    if 'item' not in request.POST or not request.POST['item']:
        context['error'] = 'You must enter an item to add.'
        return render(request, 'todolist2/index.html', context)

    new_item = Item(text=request.POST['item'], user=request.user, ip_addr=request.META['REMOTE_ADDR'])
    new_item.save()
    return redirect('todolist')


# Action for the /todolist2/delete-item route.
@login_required
def delete_action(request, item_id):
    if not request.user.email.endswith("@andrew.cmu.edu"):
        return render(request, 'todolist2/unauthorized.html')

    context = { 'items': Item.objects.all() }

    if request.method != 'POST':
        context['error'] = 'Deletes must be done using the POST method'
        return render(request, 'todolist2/index.html', context)

    # Deletes the item if present in the todo-list database.
    try:
        item_to_delete = Item.objects.get(id=item_id)
        if request.user.username != item_to_delete.user.username:
            context['error'] = 'You can only delete items you have created.'
            return render(request, 'todolist2/index.html', context)

        item_to_delete.delete()
        return redirect('todolist')
    except Item.DoesNotExist:
        context['error'] = 'The item did not exist in the To Do List.'
        return render(request, 'todolist2/index.html', context)
