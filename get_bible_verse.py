#!/usr/bin/env python

import os
import json
import datetime

import requests
# import suds

class BibleVerseGrabber(object):
    def __init__(self):
        self.translation = os.getenv('BIBLE_TRANSLATION', 'ESV')
        
        verse_date_string = os.environ.get('VERSE_DATE')
        if not verse_date_string:
            print "VERSE_DATE Environment Variable not set."
            self.__del__()

        verse_date = datetime.datetime.strptime(verse_date_string, '%Y-%m-%d')
        verse_date = verse_date.date()
        today = datetime.datetime.now().date()
        time_delta = today - verse_date

        if time_delta.days < 1:
            self.__del__()


        today_string = datetime.datetime.strftime(today, '%Y-%m-%d')
        os.environ['VERSE_DATE'] = today_string

    def __del__(self):
        pass
        
    def _make_request(self):

        if self.translation == 'ESV':
            api_url = "http://www.esvapi.org/v2/rest/verse?key=IP&include-footnotes=false&output-format=plain-text"
        response = requests.get(api_url)
        print response.text

if __name__ == '__main__':
    verse_grab = BibleVerseGrabber()

    verse_grab._make_request()
