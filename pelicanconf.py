#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'The Tor Project'
SITENAME = u'OONI'
SITEURL = ''

STATIC_PATHS = ['media']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('The Tor Project', 'https://torproject.org/'),
          ('OONI Documentation', 'http://ooni.torproject.org/docs/'),
          ('OONI Reports', 'https://ooni.torproject.org/reports/'),)

DEFAULT_PAGINATION = 10

THEME = 'theme/ooni.nu/'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
