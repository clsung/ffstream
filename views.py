from django.template import RequestContext
from django.shortcuts import render_to_response
import forms
import settings
import json
import plurk

def are_friends(userA, userB):
    url = '/FriendsFans/getFriendsByOffset'
    uid_A = get_user_id(userA)
    uid_B = get_user_id(userB)
    friends = json.loads(plurk.callAPI(url,user_id=uid_A,limit=5000).read())
    for friend in friends:
        if uid_B == friend['uid']:
            return True
    return False

def get_user_id(nickname):
    result = json.loads(plurk.callAPI('/Profile/getPublicProfile',
        user_id=nickname).read())
    return result['user_info']['uid']


def friendship(req):
    form = forms.input_form()
    is_f = False
    userA = ''
    userB = ''
    if req.method == 'POST':
        form = forms.input_form(req.POST)
        if form.is_valid():
            is_f = are_friends(form.cleaned_data['userA'],
            form.cleaned_data['userB'])
            userA = form.cleaned_data['userA']
            userB = form.cleaned_data['userB']
        
    return render_to_response('friendship.html',
            RequestContext(req,{ 'form': form, 'is_f': is_f,
                'userA': userA, 'userB': userB, }))
