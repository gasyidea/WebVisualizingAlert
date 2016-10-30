# -*-coding:utf-8-*-

from django import forms;

class CheckUrlForm(forms.Form):
    url = forms.URLField(label='URL à verifier', max_length=400)
