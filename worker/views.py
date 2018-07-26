from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from worker.models import Worker
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def profile(request):
    worker = Worker.objects.get(id=request.session['worker_id'])
    return render(request, 'profile.html', {"worker":worker})