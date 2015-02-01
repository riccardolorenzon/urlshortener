from django.db import models
from django import forms
from django.core.validators import URLValidator

class Word(models.Model):
    '''
    list all words loaded via fixture
    '''
    word_text = models.CharField(max_length = 255, primary_key=True)
    url = models.CharField(max_length = 2000, db_index=True, null=True, blank=True)
    creation_date =  models.DateTimeField(auto_now=True, null=True)

class UrlForm(forms.Form):
    url = forms.CharField(label='url', max_length=2000, validators=[URLValidator()])