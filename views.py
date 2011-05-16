from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response
import forms
import settings

def is_friends(userA, userB):
    return False

def friendship(req):
    form = forms.input_form()
    if req.method == 'POST':
        form = forms.input_form(req.POST)
    return render_to_response('friendship.html',
            RequestContext(req,form))
