from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from urlshortener_app.models import Word
import datetime
import re
import dateutil.tz
from models import UrlForm
from django.db.models import Min
from urlparse import urljoin
from django.http import Http404

def get_shorter_word(url):
    original_url = url
    #remove http or https prefix if present
    if '//' in url:
        url = url.split('//')[1]
    #get all tokens (i.e. separated words containing chars of the range [0-9a-z]
    url_tokens = re.findall(r'[0-9a-z]+', url)
    #get the queryset containing all objects(ref)
    words = Word.objects.all().order_by('word_text')
    final_word = None
    for token in url_tokens:
        #get the queryset making an exact match based on the token value
        word = words.filter(word_text = token)
        if word.count() != 0:
            word_obj = word[0]
            if word_obj.url == None:
                final_word = word[0]
                #found the word, get out of the loop
                break

    if final_word == None:
        #no words found, get first word without url
        word = words.filter(url = None)
        if word.count() != 0:
            final_word = word[0]
        else:
            #no words found, get oldest association word-url
            final_word = words.filter().annotate(Min('creation_date')).order_by('creation_date')[0]
    final_word.url = original_url
    final_word.creation_date = datetime.datetime.now(dateutil.tz.tzutc())
    final_word.save()
    return final_word.word_text

def redirect_short_url(request, short_url):
    result = Word.objects.filter(word_text = short_url)
    if result.count() == 0:
        raise Http404
    else:
        return HttpResponseRedirect(result[0].url)

def index(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = ''
            if form.data['url'] != None and form.data['url'] != '':
                full_path  = 'http' + ('', 's')[request.is_secure()] +'://' + request.META['HTTP_HOST']
                result = Word.objects.filter(url = form.data['url'])
                if result.count() == 0:
                    url = urljoin(full_path, get_shorter_word(form.data['url']))
                else:
                    url = urljoin(full_path, result[0].word_text)
            return render(request, 'home.html', {'form': form, 'url': url })
    else:
        form = UrlForm()

    return render(request, 'home.html', {'form': form})