from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotificationForm
from .models import Notification

def add_notification(request):
    form_mode = "Email"  # default mode
    if request.method == "POST":
        # Determine mode from POST data
        form_mode = request.POST.get("type", "Email")
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_notification')
    else:
        form = NotificationForm(initial={'type': form_mode})

    notifications = Notification.objects.all()
    return render(request, 'home.html', {
        'form': form,
        'form_mode': form_mode,
        'notifications': notifications,
    })

def delete_notification(request, id):
    notification = get_object_or_404(Notification, id=id)
    notification.delete()
    return redirect('add_notification')
