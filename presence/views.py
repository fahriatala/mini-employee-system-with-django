from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from worker.models import Worker
from presence.models import Presence,Permit
from presence.forms import PermitForm

from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from employee.sql_function import (
    sql_Proc,
)
from employee.functions import (
    check_array_null,
)
from django.views.decorators.csrf import csrf_exempt
import json
import simplejson

@login_required(login_url=settings.LOGIN_URL)
def presence_list(request):
    presence_list = None

	

    if request.method == 'POST':
        month = request.POST['month']
        year = request.POST['year']
        presence_list = Presence.objects.filter(time__year=year, time__month=month, worker__id=request.session['worker_id'])

    return render(request, 'presence_list.html', {'presence_list':presence_list})

@csrf_exempt
def presence_list2(request):
    if request.method == 'GET':
      result = {"data":[{"id":'permit',"nama":"Permit"},{"id":'leave',"nama":"Leave"}]}
      return HttpResponse(json.dumps(result), content_type='application/json')

@login_required(login_url=settings.LOGIN_URL)
def permit_application(request):
    if request.method == 'POST':
        form_data = request.POST
        form = PermitForm(form_data)
        if form.is_valid():
            permit = Permit(
                    worker = Worker.objects.get(id=request.session['worker_id']),
                    presence_type = request.POST['presence_type'],
                    begin_time = request.POST['begin_time'],
                    end_time = request.POST['end_time'],
                    reason = request.POST['reason'],
                    approvement = False,
                )
            permit.save()
            return redirect('/permit_application/')
    else:
        form = PermitForm()

    return render(request, 'add_permit.html', {'form':form})

@login_required(login_url=settings.LOGIN_URL)
def permit_list(request):
    permit_list = Permit.objects.filter(worker__id=request.session['worker_id'])
    return render(request, 'permit_list.html', {'permit_list':permit_list})

@login_required(login_url=settings.LOGIN_URL)
def edit_permit(request, pk):
    permit = get_object_or_404(Permit, pk=pk)
    
    if request.method == 'POST':
        post_form = PermitForm(request.POST, instance=permit)
        if post_form.is_valid():
            post_form.save()
            return redirect('/permit_list/')
    else:
        form = PermitForm()
        permit_list = Permit.objects.filter(pk=pk)
    
    return render(request,'edit_permit.html', {'permit_list':permit_list,'form':form })

def delete(request, pk):
    permit = Permit.objects.get(pk=pk)
    permit.delete()
    messages.add_message(request,messages.SUCCESS,"Delete Succeeded!")
    return HttpResponseRedirect('/permit_list/')