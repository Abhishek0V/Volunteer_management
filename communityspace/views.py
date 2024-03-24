from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
# Create your views here.



def community(request):
    messages = Message.objects.all()
    return render(request, 'community/chat.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        message_text = request.POST.get('content')
        if message_text:
            Message.objects.create(user=request.user, message_text=message_text)
    return redirect('community')

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.user == request.user:
        message.delete()
    return redirect('community')