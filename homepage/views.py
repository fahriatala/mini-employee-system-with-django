from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from worker.models import Account, Worker

# Create your views here.

def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    account = Account.objects.get(account=user.id)
                    login(request, user)

                    request.session['worker_id'] = account.worker.id
                    request.session['account_type'] = account.account_type
                    request.session['username'] = request.POST['username']
                except:
                    messages.add_message(request, messages.INFO, 'Wrong Account, Please Call The Administrator')
                return redirect('/')
            else:   
                messages.add_message(request, messages.INFO, 'user has not been verified')
        else:
            messages.add_message(request, messages.INFO, 'Wrong Password or Username')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')