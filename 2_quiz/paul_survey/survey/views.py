#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from survey.models import *
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            vt = form.cleaned_data['vote']
            s = Survey(vote=vt)
            s.save()
            results = {
                'total': Survey.objects.all().count(), 'A': Survey.get_all_A(),
                'B': Survey.get_all_B(), 'C': Survey.get_all_C(), 'D': Survey.get_all_D()}

            return render_to_response('result.html', {'results': results})
    else:
        form = SurveyForm()
    return render(request, 'survey.html', {
        'form': form,
    })
