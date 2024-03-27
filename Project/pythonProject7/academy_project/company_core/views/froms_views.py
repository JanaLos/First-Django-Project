from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from ..forms import MyForm
from ..forms import *


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        # print('Request type', type(request))
        if form.is_valid():         #zpracuje data z form.cleaned_data
            field1_data = form.cleaned_data ['field1']
            field2_data = form.cleaned_data['field1']
        return redirect('memebers')     #members - jsou z urls name=

    # else:
    form = MyForm()

    return render(request,  'basicform.html', {'form': form})


def member_form(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')

    else:
        form = MemberForm()

    return render(request, 'member_form.html', {'from': form})

