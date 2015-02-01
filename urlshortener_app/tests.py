from django.test import TestCase
from models import Word
import dateutil.tz
import datetime
import views

class UrlShortenerTestCase(TestCase):
    def setUp(self):
        Word.objects.create(word_text = 'testword', url = None, creation_date= datetime.datetime.now(dateutil.tz.tzutc()))
        Word.objects.create(word_text = 'otherword', url = None, creation_date= datetime.datetime.now(dateutil.tz.tzutc()))

    def test_url_not_in_archive(self):
        '''
        url is correctly associated with the word
        :return:
        '''
        word_text = views.get_shorter_word('http://www.example.com/testword/')
        self.assertEqual(word_text, 'testword')


    def test_url_in_archive_free_words_available(self):
        '''
        url is associated with the first word available
        :return:
        '''
        word = Word.objects.filter(word_text = 'testword')[0]
        word.url = 'http://www.example.com/testword'
        word.save()
        word_text = views.get_shorter_word('http://www.example.com/testword')
        self.assertEqual(word_text, 'otherword')


    def test_url_in_archive_no_words_available(self):
        '''
        url is associated with the oldest word
        :return:
        '''
        word = Word.objects.filter(word_text = 'testword')[0]
        word.url = 'http://www.example.com/testword'
        word.creation_date = datetime.datetime.now(dateutil.tz.tzutc())
        word.save()
        other_word = Word.objects.filter(word_text = 'otherword')[0]
        other_word.url = 'http://www.example.com/otherword'
        other_word.creation_date = datetime.datetime(2010,1,1,0,0,0,0,dateutil.tz.tzutc())
        word_text = views.get_shorter_word('http://www.example.com/testword')
        self.assertEqual(word_text, 'otherword')