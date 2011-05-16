from django import forms

class input_form(forms.Form):
    userA = forms.CharField(max_length=50, required=True,
            error_messages={'required':'User Name is required'})
    userB = forms.CharField(max_length=50, required=True,
            error_messages={'required':'User Name is required'})
