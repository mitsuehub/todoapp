# -*- coding: utf-8 -*-
from django import forms

class TodoForm(forms.Form):
    do = forms.CharField(label='やること', required=False)

